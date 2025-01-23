from django.db import models
from django.conf import settings
from django.utils import timezone

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    stripe_charge_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment of {self.amount} by {self.user}"