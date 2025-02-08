from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    get_rating = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'
    
    def get_category_name(self, obj):
        return list(obj.category.values_list("name", flat=True))
        
class CartSerializer(serializers.ModelSerializer):
    product_img = serializers.SerializerMethodField()
    product_title = serializers.CharField(source="product.title", read_only=True)
    product_price = serializers.DecimalField(source="product.price", max_digits=7, decimal_places=1, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        
    def get_product_img(self, obj):
        return f"https://snap-buy-backend.vercel.app/{obj.product.img.url}"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"