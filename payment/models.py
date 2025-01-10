from django.db import models
from product.models import Cart
from django.contrib.auth.models import User
from product.models import Product

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=50)
    Order = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    tran_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):  
        return self.name
    
class OrderdItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buying_time = models.DateTimeField(auto_now_add=True)
    tran_id = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
    
