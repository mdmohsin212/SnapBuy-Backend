from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    

class RegistrationSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    def save(self):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        conf_password = self.validated_data['confirm_password']

        if password != conf_password:
            raise serializers.ValidationError({'Error': "The passwords you entered do not match. Please try again"})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Error': "An account with this email address already exists. Please use a different email or log in."})

        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"         