from django.shortcuts import render
from events.models import Event

def organizer_dashboard(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'users/dashboard.html', {'events': events})