from django.shortcuts import redirect
from .serializers import *
from .models import *
from rest_framework import viewsets
from sslcommerz_lib import SSLCOMMERZ
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
import random, string

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all()   
    serializer_class = CheckoutSerializers
        
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
        print(data.tran_id)
        post_body = {
            'total_amount': data.total_amount,
            'currency': "BDT",
            'tran_id': data.tran_id,
            'success_url': f"https://snapbuy-backend.onrender.com/payment/payment-success/{user_id}/",
            'fail_url': "https://snapbuy-frontend.onrender.com/cart",
            'cancel_url': "https://snapbuy-frontend.onrender.com/cart",
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
        return Response({'payment_url': response['GatewayPageURL']}, status=status.HTTP_200_OK)


class PaymentSuccessView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        try:
            payment_data = request.data
            tran_id = payment_data.get('tran_id')
            checkout = Checkout.objects.filter(tran_id=tran_id, Order=False).first()

            if checkout:
                checkout.Order = True
                checkout.status = "COMPLETE"
                checkout.save()
                carts = Cart.objects.filter(user_id=user_id)
                carts.delete()

                return HttpResponseRedirect('https://snapbuy-frontend.onrender.com/profile')

            return Response({'error': 'Transaction not found or invalid.'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error': "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderdItem.objects.all()   
    serializer_class = OrderItemSerializres