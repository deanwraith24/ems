from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('stripe-payment/', views.stripe_payment, name='stripe_payment'),
    path('success/', views.success, name='success'),  # Success page route
    path('cancel/', views.cancel, name='cancel'),    # Cancel page route
]