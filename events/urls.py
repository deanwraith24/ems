from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('<int:event_id>/purchase/', views.purchase_tickets, name='purchase_tickets'),
    path('<int:event_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('organizer-dashboard/', views.organizer_dashboard, name='organizer_dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('events/', views.event_list, name='event_list'),
    path('remove/', views.remove_event, name='remove_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
]