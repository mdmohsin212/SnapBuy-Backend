from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_category_name(self, obj):
        return [category.name for category in obj.category.all()]
        
class CartSerializer(serializers.ModelSerializer):
    product_img = serializers.SerializerMethodField()
    product_title = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = '__all__'
        
    def get_product_img(self, obj):
        data = ProductSerializer(obj.product).data.get('img')
        return f"https://snapbuy-backend.onrender.com{data}"
    
    def get_product_title(self, obj):
        return ProductSerializer(obj.product).data.get('title')
    
    def get_product_price(self, obj):
        return ProductSerializer(obj.product).data.get('price')
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"