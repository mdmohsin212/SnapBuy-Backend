from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()

router.register('list', ProductViewSet, basename='list')
router.register('category', CategoryViewSet, basename='category')
router.register('cart', CartViewSet, basename='cart')
router.register('review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]   