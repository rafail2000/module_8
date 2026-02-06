from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_information_about_subscription(email):
    """
    Отправка сообщения пользователю об обновлении курса
    """

    send_mail(
        "Вышло обновление курса в ваших подписках",
        "Тело письма",
        EMAIL_HOST_USER,
        [email],
    )


@shared_task
def deactivation_user_after_month():
    """
    Установка статуса пользователя после месяца не активности на False
    """

    today = timezone.now().today().date()
    users = User.objects.all()
    for user in users:
        delta = today - user.last_login
        days_difference = delta.days
        if days_difference > 30:
            user.is_active = False
