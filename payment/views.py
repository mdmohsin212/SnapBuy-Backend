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
    
    def create(self, request, *args, **kwargs):
        user = request.data.get("user")
        order = request.data.get("Order", False)
        
        item = Checkout.objects.filter(user=user, Order=order).first()
        if item:
            serializer = self.get_serializer(item, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
    
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
        data.tran_id = unique_transaction_id_generator()
        post_body = {
            'total_amount': data.total_amount,
            'currency': "BDT",
            'tran_id': data.tran_id,
            'success_url': "127.0.0.1:8000/payment/payment-webhook",
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


class PaymentWebhookView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        try:
            payment_data = request.data
            tran_id = payment_data.get('tran_id')

            checkout = Checkout.objects.filter(tran_id=tran_id, Order=False).first()

            if checkout:
                checkout.Order = True
                checkout.status = "success"
                checkout.save()

                carts = checkout.cart.all()
                for cart in carts:
                    cart.delete()

                return HttpResponseRedirect('https://snapbuy-frontend.onrender.com/')

            return Response({'error': 'Transaction not found or invalid.'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
