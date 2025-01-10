from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('checkout', CheckoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('make_payment/<int:user_id>/', payment.as_view(), name='make_payment'),
    path('payment-webhook/', PaymentWebhookView.as_view(), name='payment-webhook'),
]