from django.contrib import admin
from .models import Checkout, OrderdItem

# Register your models here.

admin.site.register(Checkout)
admin.site.register(OrderdItem)