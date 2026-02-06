from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Модель пользователя
    """

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите телефон",
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Введите город",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )
    last_login = models.DateTimeField(
        default=timezone.now,
        verbose_name="Последний вход",
        help_text="Дата и время последнего входа пользователя",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """
    Модель платежа
    """

    amount = models.PositiveIntegerField(
        verbose_name="Сумма платежа",
        help_text="Введите сумму платежа",
    )
    session_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Id сессии",
        help_text="Укажите id сессии",
    )
    link = models.URLField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.amount
