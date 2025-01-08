from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .serializers import *
from .models import *

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                token,_ = Token.objects.get_or_create(user=user)
                login(request, user)
                print(request.user.auth_token)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' :'The provided credentials are invalid. Please check your email and password and try again.'})
        return Response(serializer.errors)


class RegistationView(APIView):
    serializer_class = RegistrationSerializers
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            link = f"http://127.0.0.1:8000/user/activate/{uid}/{user_token}"

            email_sub = "Activate your Account"
            email_body = render_to_string('confirme_mail.html',{'confirm_link' : link, 'user' : user})
            email = EmailMultiAlternatives(email_sub, '', to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response("A confirmation email has been sent to your registered email address.")
        return Response(serializer.errors)

    
class LogoutView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')

def activate_user(request, uid64, token):
    try:    
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect('register')