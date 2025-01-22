from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.redirect_page, name='redirect_page'),  # Selection page
    path('dashboard/', views.event_dashboard, name='event_dashboard'),  # CRUD area
    path('browse/', views.event_browsing, name='event_browsing'),  # Event list
]
