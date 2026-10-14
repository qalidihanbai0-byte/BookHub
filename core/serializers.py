
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

    isbn = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        max_length=13,
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

    def validate_isbn(self, value):
        if value is None or not value.strip():
            return None

        value = value.strip()

        queryset = Book.objects.filter(isbn=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Книга с таким ISBN уже существует."
            )

        return value
