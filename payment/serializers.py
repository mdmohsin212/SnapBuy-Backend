from rest_framework import serializers
from .models import *
from product.serializers import *

class CheckoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
        
class OrderItemSerializres(serializers.ModelSerializer):
    product_title = serializers.SerializerMethodField()
    class Meta:
        model = OrderdItem
        fields = "__all__"
        
    def get_product_title(self, obj):
        return ProductSerializer(obj.product).data.get('title')