import datetime
from django.db import models
from django.utils import timezone



# Create your models here.

class Ticket(models.Model):
    vehicle_types = (('Car', 'Car'), ('Motorcycle', 'Motorcycle'), ('Truck', 'Truck'))
    ticket_statuses = (('New', 'New'), ('Ongoing', 'Ongoing'), ('Finished', 'Finished'))

    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=14)
    client_email = models.EmailField(max_length=100)
   # client_email = models.CharField(max_length=100)

    vehicle_type = models.CharField(max_length=20, choices=vehicle_types, default='Car')
    vehicle_ID = models.CharField(max_length=17)
    vehicle_licence_number = models.CharField(max_length=12)
    vehicle_issue_text = models.TextField()

    ticket_status = models.CharField(max_length=10, choices=ticket_statuses, default='New')
    #ticket_entry_date = models.DateTimeField('Entry Date')
    ticket_entry_date = models.DateTimeField(default=timezone.now())
    ticket_solution_date = models.DateTimeField(null=True, blank=True)
    ticket_solution_text = models.TextField(null=True, blank=True)
    ticket_number = models.AutoField(primary_key=True)
    ticket_assignee = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name

    def __iter__(self):
        return self
