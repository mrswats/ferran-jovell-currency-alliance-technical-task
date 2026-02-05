from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=100)
    isbn_13 = models.CharField(max_length=13, unique=True)
    isbn_10 = models.CharField(max_length=10)
    language = models.CharField(max_length=50)
    date_published = models.DateField()

    def __str__(self) -> str:
        return self.title
