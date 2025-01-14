from django.contrib import admin
from .models import Event

# Register the Event model to make it available in the admin panel
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'organizer', 'ticket_price', 'tickets_available']
    search_fields = ['title', 'location', 'organizer']
    list_filter = ['date', 'organizer']

admin.site.register(Event, EventAdmin)