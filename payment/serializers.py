from rest_framework import serializers
from .models import *

class CheckoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"