from django.db import models


class Course(models.Model):
    """
    Модель курса
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    photo = models.ImageField(
        upload_to="course/photo",
        verbose_name="Фото",
        blank=True,
        null=True,
        help_text="Загрузите фото",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="описание",
        help_text="Введите описание курса",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец курса",
        help_text="Введите владельца курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Модель урока
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Курс",
        help_text="Выберете курс",
        related_name="lessons",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )
    photo = models.ImageField(
        upload_to="lesson/photo",
        verbose_name="Фото",
        blank=True,
        null=True,
        help_text="Загрузите фото",
    )
    link = models.CharField(
        max_length=100,
        verbose_name="Ссылка на видео",
        help_text="Введите ссылку на видео",
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец урока",
        help_text="Введите владельца урока",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
