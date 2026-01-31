from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import Payment, User
from users.permissions import IsOwnerOrStaff
from users.serializers import PaymentSerializer, UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Курсор для создания пользователя
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """
    Курсор для просмотра списка пользователей
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Курсор для просмотра деталей пользователя
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(UpdateAPIView):
    """
    Курсор для обновления пользователя
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class UserDestroyAPIView(DestroyAPIView):
    """
    Курсор для удаления пользователя
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class PaymentListAPIView(ListAPIView):
    """
    Курсор для просмотра списка платежей
    """

    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    serializer_class = PaymentSerializer
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("payment_date",)
