from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Ticket
from .forms import TicketForm

# Create your views here.


def index(request):
    latest_ticket_list = Ticket.objects.order_by('-ticket_number')
    paginator = Paginator(latest_ticket_list, 2)
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
    if request.method == 'POST':
        form = TicketForm(request.POST)
    else:
        form = TicketForm()
    return render(request, 'ticket/newticket.html', {'form': form})


def editticket(request, ticket_number):
    ticket = get_object_or_404(Ticket, pk=ticket_number)
    return render(request, 'ticket/editticket.html')

