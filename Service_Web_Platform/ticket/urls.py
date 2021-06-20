from django.urls import path

from . import views

app_name = 'ticket'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ticket_number>/', views.detail, name='detail'),
    path('<int:ticket_number>/editticket/', views.editticket, name='editticket'),
    path('newticket/', views.newticket, name='newticket'),
    path('newticket/ticket/index', views.index, name='index')
]