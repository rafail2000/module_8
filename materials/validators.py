from rest_framework.exceptions import ValidationError

allowed_link = "youtube.com"

def validate_allowed_link(value):
    """
    Функция для проверки на отсутствие посторонних ссылок, кроме youtube.com
    """

    if allowed_link not in value:
        raise ValidationError("Запрещено ссылаться на посторонние ресурсы, кроме YouTube")