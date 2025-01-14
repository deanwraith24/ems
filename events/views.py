from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def organizer_dashboard(request):
    # Add logic to handle the organizer dashboard
    return render(request, 'events/organizer_dashboard.html')
    
def home(request):
    # You can render a template for the home page or event list
    events = Event.objects.all()  # This will get all events from the database
    return render(request, 'events/event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})