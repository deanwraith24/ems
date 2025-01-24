import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from events.models import Event
from .models import Payment
from events.models import ShoppingCart
from django.db import models

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = ShoppingCart.objects.filter(user=request.user)
    total_value = cart_items.aggregate(total=models.Sum('total_price'))['total'] or 0.0

    return render(request, 'payments/checkout.html', {
        'cart_items': cart_items,
        'total_value': total_value
    })

def stripe_payment(request):
    user = request.user
    cart_items = ShoppingCart.objects.filter(user=user)
    total_value = cart_items.aggregate(total=models.Sum('total_price'))['total'] or 0.0

    # Stripe payment session
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.event.name,
                        },
                        'unit_amount': int(item.event.ticket_price * 100),  # Convert dollars to cents
                    },
                    'quantity': item.quantity,
                }
                for item in cart_items
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/payments/success/'),
            cancel_url=request.build_absolute_uri('/payments/cancel/'),
        )
        return redirect(session.url, code=303)

    except Exception as e:
        return render(request, 'payments/error.html', {'error': str(e)})

def success(request):
    # Clear the cart for the current user
    if request.user.is_authenticated:
        ShoppingCart.objects.filter(user=request.user).delete()

    return render(request, 'payments/success.html')

def cancel(request):
    return render(request, 'payments/cancel.html')