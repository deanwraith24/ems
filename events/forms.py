from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Event
        fields = ['name', 'description', 'image', 'date', 'location', 'ticket_price', 'tickets_available']
