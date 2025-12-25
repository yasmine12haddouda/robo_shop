
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('COD', 'الدفع عند الاستلام'),
        ('BARIDI', 'BaridiMob'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    state = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.phone}"
