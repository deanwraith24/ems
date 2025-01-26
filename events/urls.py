from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.redirect_page, name='redirect_page'),  # Selection page
    path('browse/', views.browse_events, name='browse_events'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('cart/', views.view_cart, name='shopping_cart'),
    path('add-to-cart/<int:event_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('delete-multiple-events/', views.delete_multiple_events, name='delete_multiple_events'),

]