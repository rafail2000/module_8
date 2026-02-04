from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """
    Класс для тестирования урока
    """

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            name="name course", description="description course"
        )
        self.lesson = Lesson.objects.create(
            name="name lesson",
            course=self.course,
            description="description lesson",
            link="test.youtube.com",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """
        Тест для вывода урока
        """

        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        """
        Тест создания урока
        """

        url = reverse("materials:lessons_create")
        data = {"name": "Тестовый урок", "link": "youtube.com"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """
        Тест обновления урока
        """

        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {"name": "Тестовый урок update_1"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Тестовый урок update_1")

    def test_lesson_delete(self):
        """
        Тест удаление урока
        """

        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """
        Тест списка уроков
        """

        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "link": self.lesson.link,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "photo": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class CourseTestCase(APITestCase):
    """
    Класс для тестирования курса
    """

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(
            name="name course", description="description course", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="name lesson",
            course=self.course,
            description="description lesson",
            link="test.youtube.com",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """
        Тест для вывода курса
        """

        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_course_create(self):
        """
        Тест создания курса
        """

        url = reverse("materials:course-list")
        data = {"name": "Тестовый курс", "description": "Тестовое описание курса"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        """
        Тест обновления курса
        """

        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {"name": "Тестовый курс update_1"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Тестовый курс update_1")

    def test_course_delete(self):
        """
        Тест удаление курса
        """

        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        """
        Тест списка курсов
        """

        url = reverse("materials:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "lesson": [
                        {
                            "id": self.lesson.pk,
                            "link": self.lesson.link,
                            "name": self.lesson.name,
                            "description": self.lesson.description,
                            "photo": None,
                            "course": self.course.pk,
                            "owner": self.user.pk,
                        }
                    ],
                    "name": self.course.name,
                    "photo": None,
                    "description": self.course.description,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
