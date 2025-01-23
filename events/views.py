from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ShoppingCart, Event
from .forms import EventForm
from django.contrib import messages
from django.http import JsonResponse
import json

@login_required
def redirect_page(request):
    return render(request, 'events/redirect_page.html')

@login_required
def dashboard(request):
    events = request.user.events.all()
    return render(request, 'events/dashboard.html', {'events': events})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')
    return render(request, 'events/delete_event.html', {'event': event})

def browse_events(request):
    events = Event.objects.all()  # Fetch all events from all users
    return render(request, 'events/browse.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def shopping_cart(request):
    return render(request, 'events/shopping_cart.html')

# Add to Cart
def add_to_cart(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity < 1 or quantity > event.ticket_quantity:
                messages.error(request, "Invalid ticket quantity.")
                return redirect('event_detail', event_id=event.id)

            total_price = event.ticket_price * quantity

            # Create or update cart item
            cart_item, created = ShoppingCart.objects.get_or_create(
                user=request.user, event=event,
                defaults={'quantity': quantity, 'total_price': total_price}
            )

            if not created:
                # Update existing item
                cart_item.quantity += quantity
                if cart_item.quantity > event.ticket_quantity:
                    messages.error(request, "Not enough tickets available.")
                    return redirect('event_detail', event_id=event.id)
                cart_item.total_price = cart_item.quantity * event.ticket_price
                cart_item.save()

            messages.success(request, f"{quantity} tickets added to your cart!")
        except ValueError:
            messages.error(request, "Invalid input.")
        return redirect('event_detail', event_id=event.id)
    return redirect('events:browse_events')

# Update Cart (Update ticket quantity)
def update_cart(request, cart_item_id):
    if request.method == "POST":
        try:
            cart_item = ShoppingCart.objects.get(id=cart_item_id)
            data = json.loads(request.body)
            new_quantity = int(data.get("quantity"))

            if new_quantity > 0:
                cart_item.quantity = new_quantity
                cart_item.save()

                item_total = cart_item.quantity * cart_item.event.ticket_price
                cart_total = sum(
                    item.quantity * item.event.ticket_price for item in ShoppingCart.objects.filter(user=request.user)
                )

                return JsonResponse({
                    "success": True,
                    "item_total": f"{item_total:.2f}",
                    "total_value": f"{cart_total:.2f}"
                })
            else:
                return JsonResponse({"success": False, "error": "Invalid quantity."})
        except ShoppingCart.DoesNotExist:
            return JsonResponse({"success": False, "error": "Cart item not found."})
    return JsonResponse({"success": False, "error": "Invalid request method."})

# Remove from Cart
def remove_from_cart(request, cart_item_id):
    if request.method == "POST":
        try:
            cart_item = ShoppingCart.objects.get(id=cart_item_id)
            cart_item.delete()

            cart_total = sum(
                item.quantity * item.event.ticket_price for item in ShoppingCart.objects.filter(user=request.user)
            )

            return JsonResponse({
                "success": True,
                "total_value": f"{cart_total:.2f}"
            })
        except ShoppingCart.DoesNotExist:
            return JsonResponse({"success": False, "error": "Cart item not found."})
    return JsonResponse({"success": False, "error": "Invalid request method."})

# View Cart
def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure user is logged in

    cart_items = ShoppingCart.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.info(request, "Your cart is empty.")
        return render(request, 'events/shopping_cart.html', {'cart_with_events': []})

    cart_with_events = []
    total_value = 0
    for item in cart_items:
        event = item.event
        cart_with_events.append((item, event))
        total_value += item.total_price

    return render(request, 'events/shopping_cart.html', {
        'cart_with_events': cart_with_events,
        'total_value': total_value
    })