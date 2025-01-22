from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.redirect_page, name='redirect_page'),  # Selection page
    path('browse/', views.event_browsing, name='event_browsing'),  # Event list
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
