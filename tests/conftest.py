import pytest
from rest_framework import test

from alexandria.shelves import models


@pytest.fixture
def client() -> test.APIClient:
    return test.APIClient()


@pytest.fixture
def author() -> models.Author:
    return models.Author.objects.create(
        name="Edgar Allan Poe",
    )


@pytest.fixture
def book(author: models.Author) -> models.Book:
    return models.Book.objects.create(
        title="The Raven",
        author=author,
    )
