from rest_framework import viewsets

from alexandria.shelves import models
from alexandria.shelves import serializers


class AuthorViewSet(viewsets.ModelViewSet[models.Author]):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewSet(viewsets.ModelViewSet[models.Book]):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
