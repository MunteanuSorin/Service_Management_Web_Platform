import django_filters
from .models import Ticket


class TicketFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(lookup_expr='icontains')
    ticket_assignee = django_filters.CharFilter(lookup_expr='icontains')
    vehicle_licence_number = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ticket
        fields = ['ticket_number', 'ticket_assignee', 'ticket_status',
                  'client_name', 'client_phone',
                  'vehicle_type', 'vehicle_licence_number']
