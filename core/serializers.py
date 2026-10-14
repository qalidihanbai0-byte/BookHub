
from rest_framework import serializers

from .models import Author, Book, Tag


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "biography",
            "birth_date",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "description",
        ]
        read_only_fields = ["id"]


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(
        source="author.name",
        read_only=True,
    )
    tags_details = TagSerializer(
        source="tags",
        many=True,
        read_only=True,
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "author",
            "author_name",
            "tags",
            "tags_details",
            "published_date",
            "isbn",
            "rating",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
