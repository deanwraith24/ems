from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:event_id>/', views.checkout, name='checkout'),
]
