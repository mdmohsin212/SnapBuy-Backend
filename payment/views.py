from .serializers import *
from .models import *
from rest_framework import viewsets
from sslcommerz_lib import SSLCOMMERZ
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework import filters

class Search(filters.BaseFilterBackend):
    def filter_queryset(self,request, query_set, view):
        user_id = request.query_params.get("user_id")
        if user_id:
            return query_set.filter(user__id=user_id)
        return query_set


class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.select_related("user").prefetch_related("cart__product")
    serializer_class = CheckoutSerializers
    permission_classes = [AllowAny]
    filter_backends = [Search]

        
class payment(APIView):
    def post(self, request, user_id, *args, **kwargs):
        user = User.objects.get(id=user_id)
        data = Checkout.objects.filter(user=user, Order=False).first()
        settings = {
            'store_id': 'snapb6780925c46a95',
            'store_pass': 'snapb6780925c46a95@ssl',
            'issandbox': True,
        }
        sslcz = SSLCOMMERZ(settings)
        post_body = {
            'total_amount': data.total_amount,
            'currency': "BDT",
            'tran_id': data.tran_id,
            'success_url': f"https://snapbuy-backend.onrender.com/payment/payment-success/{user_id}/",
            'fail_url': f"https://snapbuy-backend.onrender.com/payment/payment-failed/{user_id}/",
            'cancel_url': f"https://snapbuy-backend.onrender.com/payment/payment-failed/{user_id}/",
            'emi_option': 0,
            'cus_name': data.name,
            'cus_email': data.email,
            'cus_phone': "01700000000",
            'cus_add1': data.address,
            'cus_city': "Dhaka",
            'cus_country': "Bangladesh",
            'shipping_method': "NO",
            'multi_card_name': "",
            'num_of_item': 1,
            'product_name': "Test",
            'product_category': "Test Category",
            'product_profile': "general",
        }

        response = sslcz.createSession(post_body)
        return Response({'payment_url': response['GatewayPageURL']})


class PaymentSuccessView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            payment_data = request.data
            tran_id = payment_data.get('tran_id')
            checkout = Checkout.objects.filter(tran_id=tran_id, Order=False).first()

            if checkout:
                checkout.Order = True
                checkout.status = "COMPLETE"
                checkout.save()

                carts = Cart.objects.filter(user_id=user_id)
                for cart in carts:
                    OrderdItem.objects.create(
                        user=cart.user,
                        product=cart.product,
                        buyer_name = checkout.name,
                        email = checkout.email,
                        address = checkout.address,
                        status = checkout.status,
                        quantity = cart.quantity,
                        price=cart.product.price,
                        tran_id=tran_id
                    )
                carts.delete()                
                return HttpResponseRedirect('https://snapbuy-frontend.onrender.com/profile')

            return Response({'error': 'Transaction not found or invalid.'})

        except Exception:
            return Response({'error': "Something went wrong"})


class PaymentFailedView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        try:
            payment_data = request.data
            tran_id = payment_data.get('tran_id')
            checkout = Checkout.objects.filter(tran_id=tran_id, Order=False).first()

            if checkout:
                checkout.Order = True
                checkout.status = "FAILED"
                checkout.save()
            
            return HttpResponseRedirect('https://snapbuy-frontend.onrender.com/cart')
        
        except Exception:
            return Response({'error': "Something went wrong"})
        

class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderdItem.objects.select_related("user", "product").prefetch_related("product__category")
    serializer_class = OrderItemSerializres
    filter_backends = [Search]

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

def status(request, user_id):
    try:
        checkouts = Checkout.objects.filter(user_id=user_id).only("id", "Order")
        
        for checkout in checkouts:
            if checkout.Order == False:
                return JsonResponse({'status': "YES", 'id': checkout.id})
            
        return JsonResponse({'status': "NO"})
    except User.DoesNotExist:
        return JsonResponse({"error": "Not found user"})