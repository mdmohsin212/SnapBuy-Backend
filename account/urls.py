from django.urls import path, include
from .views import *
from .serializers import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistationView.as_view(), name='register'),
    path('activate/<uid64>/<token>/', activate_user, name='activate_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# SIAM12345