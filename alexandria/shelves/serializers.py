from rest_framework import serializers

from alexandria.shelves import models


class AuthorSerializer(serializers.ModelSerializer[models.Author]):
    class Meta:
        model = models.Author
        fields = (
            "id",
            "name",
        )


class BookSerializer(serializers.ModelSerializer[models.Book]):
    author = AuthorSerializer()

    class Meta:
        model = models.Book
        fields = (
            "id",
            "title",
            "author",
        )
