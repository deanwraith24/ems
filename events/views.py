from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EventForm
from .models import Event

def organizer_dashboard(request):
    events = Event.objects.all()
    return render(request, 'events/organizer_dashboard.html', {'events': events})
    
def home(request):
    # You can render a template for the home page or event list
    events = Event.objects.all()  # This will get all events from the database
    return render(request, 'events/event_list.html', {'events': events})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def create_event(request):
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