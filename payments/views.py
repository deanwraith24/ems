import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from events.models import Event
from .models import Payment

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request, event_name):
    event = get_object_or_404(Event, name=event_name)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        total_amount = event.ticket_price * quantity
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': event.name,
                        },
                        'unit_amount': int(total_amount * 100),  # Amount in cents
                    },
                    'quantity': quantity,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/payment/success/'),
            cancel_url=request.build_absolute_uri('/payment/cancel/'),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, 'payments/checkout.html', {'event': event})

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')