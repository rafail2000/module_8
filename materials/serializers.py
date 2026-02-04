from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import validate_allowed_link


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели урока
    """

    link = serializers.CharField(validators=[validate_allowed_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели курса
    """

    lesson = LessonSerializer(many=True, read_only=True, source="lessons")

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отдельного курса
    """

    count_lessons_from_with_course = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True, source="lessons")

    def get_count_lessons_from_with_course(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = (
            "name",
            "photo",
            "description",
            "count_lessons_from_with_course",
            "lesson",
        )
