from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Ticket
from .forms import TicketForm, EditTicketForm
from .filters import TicketFilter

# Create your views here.


def index(request):
    latest_ticket_list = Ticket.objects.order_by('-ticket_number')
    paginator = Paginator(latest_ticket_list, 15)
    context = {
        'latest_ticket_list': latest_ticket_list,
    }
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ticket/index.html', {'page_obj': page_obj})


def detail(request, ticket_number):
    ticket = get_object_or_404(Ticket, pk=ticket_number)
    return render(request, 'ticket/detail.html', {'ticket': ticket})


def newticket(request):
    form = TicketForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/ticket/')

    return render(request, 'ticket/newticket.html', {'form': form})

'''
    if request.method == 'POST':
        form = TicketForm(request.POST)
    else:
        form = TicketForm()
    return render(request, 'ticket/newticket.html', {'form': form})
'''

def editticket(request, ticket_number):
    context = {}
    ticket = get_object_or_404(Ticket, pk=ticket_number)
#    curent_data = {
#        "client_name": ticket.client_name,
#        "client_phone": ticket.client_phone,
#        "client_email": ticket.client_email,
#        "vehicle_type": ticket.vehicle_type,
#        "vehicle_ID": ticket.vehicle_ID,
#        "vehicle_licence_number": ticket.vehicle_licence_number,
#        "vehicle_issue_text": ticket.vehicle_issue_text or 'TBD',
#        "ticket_status": ticket.ticket_status,
#        "ticket_solution_date": ticket.ticket_solution_date or 'yyy-mm-dd',
#        "ticket_solution_text": ticket.ticket_solution_text or 'TBD',
#        "ticket_assignee": ticket.ticket_assignee

#    }

    form = EditTicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('/ticket/')
    context['form']=form
    return render(request, 'ticket/editticket.html', context)


def deleteticket(request, ticket_number):
    ticket = get_object_or_404(Ticket, pk=ticket_number)
    # delete the ticket directly
    Ticket.objects.filter(ticket_number=ticket_number).delete()
    return render(request, 'ticket/deleteticket.html', {'ticket': ticket})


def search(request):
    ticket_list = Ticket.objects.all()
    ticket_filter = TicketFilter(request.GET, queryset=ticket_list)
    return render(request, 'ticket/searchticket.html', {'filter': ticket_filter})


def new_client_ticket(request):
    form = TicketForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/ticket/')

    return render(request, 'ticket/clientticket.html', {'form': form})
