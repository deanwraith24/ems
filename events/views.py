from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from .models import Event, Cart
from django.http import JsonResponse

def landing_page(request):
    """
    View for the landing page. Displays featured events or all events.
    """
    events = Event.objects.all()[:5]  # Show only a limited number of events for the landing page
    return render(request, 'events/landing_page.html', {'events': events})


def home(request):
    """
    Redirect to the landing page.
    """
    return redirect('landing_page')


def event_list(request):
    """
    View for listing all events.
    """
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def organizer_dashboard(request):
    """
    View for the organizer's dashboard.
    """
    events = Event.objects.all()
    return render(request, 'events/organizer_dashboard.html', {'events': events})


def create_event(request):
    """
    View for creating a new event.
    """
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('events:organizer_dashboard')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


def remove_event(request):
    """
    View for removing events from the organizer's dashboard.
    """
    if request.method == 'POST':
        event_ids = request.POST.getlist('event_ids')
        if event_ids:
            Event.objects.filter(id__in=event_ids).delete()
            messages.success(request, 'Selected events were successfully removed.')
        else:
            messages.error(request, 'No events selected for removal.')
        return redirect('events:organizer_dashboard')
    events = Event.objects.all()
    return render(request, 'events/remove_event.html', {'events': events})


def edit_event(request, event_id):
    """
    View for editing an event.
    """
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('events:organizer_dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})


@login_required
def purchase_tickets(request, event_id):
    """
    View for purchasing tickets.
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/purchase_tickets.html', {'events': [event]})

@login_required
def add_to_cart(request, event_id):
    """
    Add tickets for an event to the cart and stay on the event page.
    """
    event = get_object_or_404(Event, id=event_id)
    quantity = int(request.POST.get('quantity', 1))

    # Check if the cart already has this event
    cart_item, created = Cart.objects.get_or_create(user=request.user, event=event)
    if not created:
        cart_item.quantity += quantity
    cart_item.save()

    # Respond with success without redirecting
    return JsonResponse({"success": True, "message": "Tickets added to cart!"})

@login_required
def view_cart(request):
    """
    View the user's shopping cart.
    """
    cart_items = Cart.objects.filter(user=request.user).select_related('event')
    return render(request, 'events/cart.html', {'cart_items': cart_items})

@login_required
def checkout(request):
    """
    View for checking out and processing payment.
    """
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    # Add payment logic here
    return render(request, 'events/checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()
    return redirect('events:cart')

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('events:cart')

@login_required
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    return redirect('events:cart')
