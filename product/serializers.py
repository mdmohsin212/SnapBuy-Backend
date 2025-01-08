from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    product_img = serializers.SerializerMethodField()
    product_title = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = '__all__'
        
    def get_product_img(self, obj):
        data = ProductSerializer(obj.product).data.get('img')
        return f"http://127.0.0.1:8000/{data}"
    
    def get_product_title(self, obj):
        return ProductSerializer(obj.product).data.get('title')