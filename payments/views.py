import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from events.models import Event  # Correctly reference the Event model from the events app

# Set up Stripe API key
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request, event_id):
    # Safely retrieve the event or return a 404 if not found
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        # Create a Stripe checkout session
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': event.name,
                        },
                        'unit_amount': int(event.ticket_price * 100),  # Convert to cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),  # Replace with the actual success route
                cancel_url=request.build_absolute_uri('/cancel/'),    # Replace with the actual cancel route
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            # Handle errors with a meaningful response
            return JsonResponse({'error': str(e)}, status=500)

    # Render the checkout page with event details
    return render(request, 'payments/checkout.html', {'event': event})
