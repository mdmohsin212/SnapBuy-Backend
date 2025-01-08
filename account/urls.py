from django.urls import path
from .views import *
from .serializers import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistationView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', activate_user, name='activate_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# SIAM123456