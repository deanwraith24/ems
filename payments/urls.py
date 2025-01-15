from django.urls import path
from . import views

app_name = 'payments'  # Ensure the app_name matches the namespace in the template

urlpatterns = [
    path('checkout/<int:event_id>/', views.checkout, name='checkout'),  # Ensure this exists
]