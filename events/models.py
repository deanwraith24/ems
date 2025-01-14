from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    tickets_available = models.PositiveIntegerField()

    def __str__(self):
        return self.name