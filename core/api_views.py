
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Author, Book, Tag
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    TagSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = (
        Book.objects
        .select_related("author")
        .prefetch_related("tags")
    )
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
