from django.urls import path, include
from .views import *
from .serializers import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('contact', ContactViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/login/', AdminLoginView.as_view(), name='adminLogin'),
    path('register/', RegistationView.as_view(), name='register'),
    path('change_password/<int:user_id>/', PasswordChangeAPIView.as_view(), name='change_password'),
    path('activate/<uid64>/<token>/', activate_user, name='activate_user'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# SIAM12345