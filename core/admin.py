
from django.contrib import admin

from .models import Author, Book, Tag


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birth_date", "created_at")
    search_fields = ("name", "biography")
    ordering = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published_date", "rating")
    list_filter = ("author", "tags", "rating")
    search_fields = ("title", "author__name", "description", "isbn")
    filter_horizontal = ("tags",)
    list_select_related = ("author",)
    ordering = ("title",)
