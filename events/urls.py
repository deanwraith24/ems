from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('organizer-dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('remove/', views.remove_event, name='remove_event'),
]