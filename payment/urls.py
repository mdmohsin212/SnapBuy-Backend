from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('checkout', CheckoutViewSet)
router.register("orderitem", OrderItemView)
router.register('shipping', ShippingViewSet, basename='shipping')

urlpatterns = [
    path('', include(router.urls)),
    path('make_payment/<int:user_id>/', payment.as_view(), name='make_payment'),
    path('payment-success/<int:user_id>/', PaymentSuccessView.as_view(), name='payment-success'),
    path('payment-failed/<int:user_id>/', PaymentFailedView.as_view(), name='payment-failed'),
    path('status/<int:user_id>/', status, name="status"),
]