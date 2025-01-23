import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from events.models import Event
from .models import Payment

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

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')