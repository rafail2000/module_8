from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """
    Сериализатор для модели урока
    """

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    """
    Сериализатор для модели курса
    """

    lesson = LessonSerializer(many=True, read_only=True, source="lessons")

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
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
