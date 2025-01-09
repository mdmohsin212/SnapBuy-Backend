from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters

# Create your views here.
class SearchItem(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        category = request.query_params.get("category")
        if category:
            return query_set.filter(category__name__iexact=category)

class CartSearch(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        user_id = request.query_params.get("user_id")
        if user_id:
            return query_set.filter(user__id=user_id)
        return query_set
        
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [CartSearch]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchItem]