from rest_framework import serializers

from alexandria.shelves import models


class AuthorSerializer(serializers.ModelSerializer[models.Author]):
    class Meta:
        model = models.Author
        fields = (
            "id",
            "name",
            "birth_date",
            "nationality",
        )


class BookSerializer(serializers.ModelSerializer[models.Book]):
    author = serializers.PrimaryKeyRelatedField(queryset=models.Author.objects.all())

    class Meta:
        model = models.Book
        fields = (
            "author",
            "date_published",
            "isdn_10",
            "isdn_13",
            "language",
            "title",
        )
