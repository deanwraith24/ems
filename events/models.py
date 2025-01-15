from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField()
    date = models.DateField(default='')
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=200)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    tickets_available = models.IntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title