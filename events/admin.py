from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Optional: Customize the list display and other admin panel features
    list_display = ('title', 'date', 'location', 'organizer')
    list_filter = ('date', 'location')  # Add filters if needed
    search_fields = ('title', 'description')  # Add search functionality
    ordering = ('date', 'time')  # Order by date and time
