from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'image', 'description', 'time', 'date', 'venue', 'ticket_price', 'ticket_quantity']
