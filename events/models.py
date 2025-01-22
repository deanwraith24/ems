from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    venue = models.CharField(max_length=255)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    ticket_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name