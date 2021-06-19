from django import forms
from django.utils import timezone
from .models import Ticket


class TicketForm(forms.Form):
    VEHICLE_CHOICES = [('Car', 'Car'),
                       ('Motorcycle', 'Motorcycle'),
                       ('Truck', 'Truck')]
    TICKET_STATUSES = [('New', 'New'),
                       ('Ongoing', 'Ongoing'),
                       ('Finished', 'Finished')]

    ticket_status = forms.CharField(label='Ticket Status', initial='New', disabled=True)
    ticket_entry_date = forms.DateTimeField(label='Ticket Entry Date', initial=timezone.now(), disabled=True)

    client_name = forms.CharField(label='Client Name', max_length=100)
    client_phone = forms.CharField(label='Phone', max_length=14)
    client_email = forms.EmailField(label='Email Address', max_length=100)

    vehicle_type = forms.ChoiceField(label='Vehicle Type', choices=VEHICLE_CHOICES, widget=forms.RadioSelect, initial='Car')
    vehicle_ID = forms.CharField(label='Vehicle ID', max_length=17)
    vehicle_licence_number = forms.CharField(label='License Number', max_length=12)
    vehicle_issue = forms.CharField(label='Vehicle Issue')

    last_ticket_number = Ticket.objects.order_by('-ticket_number')[0].ticket_number
#   last_ticket_id = last_ticket_number.ticket_number

    ticket_number = forms.IntegerField(label='Ticket Number', initial=last_ticket_number+1,
                                       disabled=True)


class Edit_Ticket_Form(forms.Form):
    VEHICLE_CHOICES = [('Car', 'Car'),
                       ('Motorcycle', 'Motorcycle'),
                       ('Truck', 'Truck')]
    TICKET_STATUSES = [('New', 'New'),
                       ('Ongoing', 'Ongoing'),
                       ('Finished', 'Finished')]

    client_name = forms.CharField(label='Client Name', max_length=100)
    client_phone = forms.CharField(label='Phone', max_length=14)
    client_email = forms.EmailField(label='Email Address', max_length=100)
    vehicle_type = forms.ChoiceField(label='Vehicle Type', choices=VEHICLE_CHOICES, widget=forms.Select, initial='Car')
    vehicle_ID = forms.CharField(label='Vehicle ID', max_length=17)
    vehicle_licence_number = forms.CharField(label='License Number', max_length=12)
    vehicle_issue_text = forms.CharField(label='Vehicle Issue', widget=forms.Textarea)
    ticket_status = forms.ChoiceField(label='Ticket Status', choices = TICKET_STATUSES, widget=forms.Select, initial=Ticket.ticket_status)
    ticket_solution_date = forms.DateTimeField(label='Ticket Solution Date', widget=forms.DateInput(format='%d/%m/%Y'), initial=Ticket.ticket_solution_date)
    ticket_solution_text = forms.CharField(label='Solution Text', widget=forms.Textarea)
    ticket_assignee = forms.CharField(label='Assignee', max_length=100)
#    ticket_entry_date = forms.DateTimeField(label='Ticket Entry Date', initial=Ticket.ticket_entry_date, disabled=True)


#    ticket_number = forms.IntegerField(label='Ticket Number', initial=last_ticket_number, disabled=True)


