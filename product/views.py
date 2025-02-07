from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import AllowAny

# Create your views here.

class CartSearch(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        user_id = request.query_params.get("user_id")
        if user_id:
            return query_set.filter(user__id=user_id)
        
        product_id = request.query_params.get("product_id")
        if product_id:
            return query_set.filter(product=product_id)
        
        category_name = request.query_params.get("category")
        if category_name:
            return query_set.filter(category__name__iexact=category_name)
        
        return query_set
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [CartSearch]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [CartSearch]
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [CartSearch]