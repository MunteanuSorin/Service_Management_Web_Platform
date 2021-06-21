from django import forms
from django.utils import timezone
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['ticket_solution_date', 'ticket_solution_text', 'ticket_assignee']

    ticket_status = forms.CharField(label='Ticket Status', initial='New', disabled=True)
    ticket_entry_date = forms.DateTimeField(label='Ticket Entry Date', initial=timezone.now(), disabled=True)


class EditTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['client_name','client_phone','client_email','vehicle_type','vehicle_ID','vehicle_licence_number','vehicle_issue_text','ticket_status', 'ticket_entry_date', 'ticket_solution_date', 'ticket_solution_text','ticket_assignee']

