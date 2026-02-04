from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.fixture
def books_url():
    return reverse("api:books-list")


@pytest.fixture
def list_books(client, books_url):
    def _():
        return client.get(books_url)

    return _


def test_books_url(books_url):
    assert books_url == "/api/books/"


@pytest.mark.django_db
def test_books_status_code(list_books):
    response = list_books()
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_books_empty_data(list_books):
    response = list_books()
    assert response.json()["results"] == []


@pytest.mark.django_db
def test_books_data(list_books, book):
    response = list_books()
    assert response.json()["results"] == [
        {
            "author": {
                "id": 1,
                "name": "Edgar Allan Poe",
            },
            "id": 1,
            "title": "The Raven",
        }
    ]


@pytest.mark.django_db
def test_books_data_number_of_queries(list_books, django_assert_num_queries):
    with django_assert_num_queries(1):
        list_books()
