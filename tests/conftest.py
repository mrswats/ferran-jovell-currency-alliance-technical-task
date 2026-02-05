from datetime import datetime

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
        birth_date=datetime(1809, 1, 19),
        nationality="american",
    )


@pytest.fixture
def book(author: models.Author) -> models.Book:
    return models.Book.objects.create(
        author=author,
        title="The Raven",
        isbn_13="9782048742975",
        date_published=datetime(2024, 9, 4),
        language="english",
    )
