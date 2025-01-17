from .models import Cart

def cart_total_value(request):
    if request.user.is_authenticated:
        total = sum(item.total_price() for item in Cart.objects.filter(user=request.user))
        return {'cart_total_value': total}
    return {'cart_total_value': 0}
