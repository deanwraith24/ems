from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'date', 'location', 'ticket_price', 'tickets_available']
