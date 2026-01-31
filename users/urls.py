from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    # user
    path('register/', UserCreateAPIView.as_view(),name='register'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # payment
    path("payments/", PaymentListAPIView.as_view(), name="payments_list"),
]
