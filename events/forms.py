from django import forms
from datetime import datetime
from .models import Event

class EventForm(forms.ModelForm):

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.today().date():
            raise forms.ValidationError("Event date cannot be in the past.")
        return date

    def clean_ticket_price(self):
        price = self.cleaned_data['ticket_price']
        if price < 0:
            raise forms.ValidationError("Ticket price cannot be negative.")
        return price

    class Meta:
        model = Event
        fields = ['name', 'image', 'description', 'time', 'date', 'venue', 'ticket_price', 'ticket_quantity']
