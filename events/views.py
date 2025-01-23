from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ShoppingCart, Event
from .forms import EventForm
from django.contrib import messages

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

def add_to_cart(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total_price = event.ticket_price * quantity
        
        # Check if the user already has this event in their cart
        cart_item, created = ShoppingCart.objects.get_or_create(
            user=request.user, event=event,
            defaults={'quantity': quantity, 'total_price': total_price}
        )
        
        # If the item already exists, update the quantity and total_price
        if not created:
            cart_item.quantity += quantity
            cart_item.total_price = cart_item.quantity * event.ticket_price
            cart_item.save()
        
        # Show success message
        messages.success(request, "Congratulations, tickets added to your cart!")
        
        # Redirect to cart page or stay on the same page
        return redirect('event_detail', event_id=event.id)

    return redirect('events:browse_events')

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure user is logged in

    cart_items = ShoppingCart.objects.filter(user=request.user)
    cart_with_events = []

    for item in cart_items:
        event = get_object_or_404(Event, id=item.event_id)  # Ensure you're getting the correct event
        if event:  # Make sure event exists and has an ID
            cart_with_events.append((item, event))
        else:
            # Handle case where event is not found (optional)
            print(f"Event with ID {item.event_id} not found")

    return render(request, 'events/shopping_cart.html', {'cart_with_events': cart_with_events})