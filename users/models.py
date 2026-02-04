from django.contrib.auth.models import AbstractUser
from django.db import models


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

    CASH = "cash"
    TRANSFER = "transfer"

    PAYMENT_METHOD_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод"),
    ]

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Выберете пользователя",
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата оплаты", help_text="Введите дату оплаты"
    )
    paid_course = models.ForeignKey(
        "materials.Course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="payd",
    )
    paid_lesson = models.ForeignKey(
        "materials.Lesson",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="payd",
    )
    payment_amount = models.FloatField(
        verbose_name="Сумма оплаты", help_text="Введите сумму оплаты"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name="Способ оплаты",
        help_text="Введите способ оплаты",
    )

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return (
            f"{self.user}, оплаченный курс - {self.paid_course},"
            f"оплаченный урок - {self.paid_lesson},"
            f"сумма оплаты - {self.payment_amount}"
        )
