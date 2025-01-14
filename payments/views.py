import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Event

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        # Create a checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': event.name,
                    },
                    'unit_amount': int(event.ticket_price * 100),  # Stripe expects the price in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return JsonResponse({'id': session.id})
    return render(request, 'payments/checkout.html', {'event': event})