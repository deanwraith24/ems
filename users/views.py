from django.shortcuts import render
from events.models import ShoppingCart

def landing_page(request):
    cart_item_count = ShoppingCart.objects.filter(user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'users/landing.html', {'cart_item_count': cart_item_count})

def signup_page(request):
    return render(request, 'users/signup.html')