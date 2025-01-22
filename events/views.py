from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def redirect_page(request):
    return render(request, 'events/redirect_page.html')

@login_required
def event_dashboard(request):
    # Logic for managing events will go here
    return render(request, 'events/dashboard.html')

@login_required
def event_browsing(request):
    # Logic for browsing events will go here
    return render(request, 'events/browse.html')
