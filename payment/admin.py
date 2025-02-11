from django.contrib import admin
from .models import Checkout, OrderdItem, Shipping

# Register your models here.

admin.site.register(Checkout)
admin.site.register(OrderdItem)
admin.site.register(Shipping)