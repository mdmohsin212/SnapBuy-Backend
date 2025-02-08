from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import AllowAny

class CartSearch(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        user_id = request.query_params.get("user_id")
        product_id = request.query_params.get("product_id")
        category_name = request.query_params.get("category")

        if user_id:
            query_set = query_set.filter(user__id=user_id)
            
        if product_id:
            query_set = query_set.filter(id=product_id)
            
        if category_name:
            query_set = query_set.filter(category__name__iexact=category_name)

        return query_set

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related("category", "review_set")
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [CartSearch]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.select_related("user", "product")
    serializer_class = CartSerializer
    filter_backends = [CartSearch]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [CartSearch]