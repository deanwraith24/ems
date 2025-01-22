from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date', 'venue', 'ticket_price', 'created_at')
    list_filter = ('date', 'venue')
    search_fields = ('name', 'venue', 'description')