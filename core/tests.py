
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from .models import Author, Book, Tag


class BookModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Тестовый автор",
            biography="Тестовая биография",
        )

        self.tag = Tag.objects.create(name="Фантастика")

        self.book = Book.objects.create(
            title="Тестовая книга",
            description="Описание тестовой книги",
            author=self.author,
            rating=8,
        )

        self.book.tags.add(self.tag)

    def test_book_has_author_and_tags(self):
        self.assertEqual(self.book.author.name, "Тестовый автор")
        self.assertEqual(self.book.tags.count(), 1)

    def test_book_string_representation(self):
        self.assertEqual(str(self.book), "Тестовая книга")


class BookWebTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Автор")

        self.book = Book.objects.create(
            title="Книга для сайта",
            description="Описание",
            author=self.author,
            rating=7,
        )

    def test_book_list_page(self):
        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Книга для сайта")

    def test_book_detail_page(self):
        response = self.client.get(
            reverse("book_detail", args=[self.book.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Книга для сайта")


class BookAPITests(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword123!",
        )

        self.client_api = APIClient()
        self.client_api.force_authenticate(user=self.user)

        self.author = Author.objects.create(name="API автор")

        self.book = Book.objects.create(
            title="API книга",
            description="Описание API книги",
            author=self.author,
            rating=9,
        )

    def test_api_book_list(self):
        response = self.client_api.get("/api/books/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "API книга")

    def test_api_book_detail(self):
        response = self.client_api.get(
            f"/api/books/{self.book.pk}/"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "API книга")

    def test_anonymous_user_cannot_create_book(self):
        anonymous_client = APIClient()

        response = anonymous_client.post(
            "/api/books/",
            {
                "title": "Запрещённая книга",
                "description": "Попытка без авторизации",
                "author": self.author.pk,
                "rating": 5,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 403)

        self.assertFalse(
            Book.objects.filter(
                title="Запрещённая книга"
            ).exists()
        )

    def test_api_create_book(self):
        response = self.client_api.post(
            "/api/books/",
            {
                "title": "Новая книга",
                "description": "Создана через API",
                "author": self.author.pk,
                "rating": 8,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 201)

        self.assertTrue(
            Book.objects.filter(title="Новая книга").exists()
        )

    def test_api_update_book(self):
        response = self.client_api.patch(
            f"/api/books/{self.book.pk}/",
            {"title": "Обновлённая книга"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)

        self.book.refresh_from_db()

        self.assertEqual(
            self.book.title,
            "Обновлённая книга",
        )

    def test_api_delete_book(self):
        response = self.client_api.delete(
            f"/api/books/{self.book.pk}/"
        )

        self.assertEqual(response.status_code, 204)

        self.assertFalse(
            Book.objects.filter(pk=self.book.pk).exists()
        )
