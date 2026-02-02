from rest_framework.serializers import ModelSerializer

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    """
    Серилизатор для пользователя
    """

    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """
    Серилизатор для платежей
    """

    class Meta:
        model = Payment
        fields = "__all__"
