from django.db import models
from product.models import Cart
from django.contrib.auth.models import User

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=50)
    Order = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return self.name