from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Ticket

# Create your views here.


def index(request):
    latest_ticket_list = Ticket.objects.order_by('-ticket_number')
    context = {
        'latest_ticket_list': latest_ticket_list,
    }
    return render(request, 'ticket/index.html', context)

def detail(request, ticket_number):
    ticket = get_object_or_404(Ticket, pk=ticket_number)
    return render(request, 'ticket/detail.html', {'ticket': ticket})

def newticket(request):
    return render(request, 'ticket/newticket.html')

def editticket(request):
    return render(request, '<int:ticket_number>/editticket.html')