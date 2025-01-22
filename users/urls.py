from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Landing Page
    path('', views.landing_page, name='landing_page'),

    # Sign-Up Page (uses Django Allauth's built-in view)
    path('signup/', TemplateView.as_view(template_name="users/signup.html"), name='signup'),

    # Login Page (uses Django Allauth's built-in view)
    path('login/', TemplateView.as_view(template_name="users/login.html"), name='login'),

    # Logout Page
    path('logout/', TemplateView.as_view(template_name="users/logout.html"), name='logout'),
]
