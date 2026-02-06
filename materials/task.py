from config.settings import EMAIL_HOST_USER
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_information_about_subscription(email):
    """
    Отправка сообщения пользователю об обновлении курса
    """

    send_mail('Вышло обновление курса в ваших подписках', 'Тело письма', EMAIL_HOST_USER, [email])
