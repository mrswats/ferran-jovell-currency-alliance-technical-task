from http import HTTPStatus
from typing import Any

import pytest
from django.urls import reverse


@pytest.fixture
def the_cat_data(author):
    return {
        "author": author.pk,
        "title": "The Cat",
        "date_published": "1843-08-19",
        "language": "english",
        "isdn_10": "6057876415",
        "isdn_13": "9786057876416",
    }


@pytest.fixture
def books_url():
    return reverse("api:books-list")


@pytest.fixture
def books_detail_url():
    def _(book_id: str) -> str:
        return reverse("api:books-detail", kwargs={"isdn_13": book_id})

    return _


@pytest.fixture
def list_books(client, books_url):
    def _():
        return client.get(books_url)

    return _


@pytest.fixture
def retrieve_books(client, books_detail_url):
    def _(book_id: str):
        return client.get(books_detail_url(book_id))

    return _


@pytest.fixture
def create_books(client, books_url):
    def _(data: dict[str, Any]):
        return client.post(books_url, data=data)

    return _


@pytest.fixture
def update_books(client, books_detail_url):
    def _(book_id: str, data: dict[str, Any]):
        return client.patch(books_detail_url(book_id), data=data)

    return _


@pytest.fixture
def delete_books(client, books_detail_url):
    def _(book_id: str):
        return client.delete(books_detail_url(book_id))

    return _


def test_books_url(books_url):
    assert books_url == "/api/books/"


def test_book_detail_url(books_detail_url):
    assert books_detail_url("isdn-13") == "/api/books/isdn-13/"


@pytest.mark.django_db
def test_books_list_status_code(list_books):
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
            "author": 1,
            "date_published": "2024-09-04",
            "isdn_13": "9782048742975",
            "isdn_10": "2048742971",
            "language": "english",
            "title": "The Raven",
        }
    ]


@pytest.mark.django_db
def test_books_list_number_of_queries(list_books, django_assert_num_queries):
    with django_assert_num_queries(1):
        list_books()


@pytest.mark.django_db
def test_books_create_status_code(create_books, the_cat_data):
    response = create_books(the_cat_data)
    assert response.status_code == HTTPStatus.CREATED, response.json()


@pytest.mark.django_db
def test_books_create_data(create_books, the_cat_data):
    response = create_books(the_cat_data)
    assert response.json() == the_cat_data


@pytest.mark.django_db
def test_books_create_number_of_queries(create_books, the_cat_data, django_assert_num_queries):
    with django_assert_num_queries(2):
        create_books(the_cat_data)


@pytest.mark.django_db
def test_books_retrieve_status_code(retrieve_books, book):
    response = retrieve_books(book.isdn_13)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_books_retrieve_data(retrieve_books, book):
    response = retrieve_books(book.isdn_13)
    assert response.json() == {
        "author": 1,
        "date_published": "2024-09-04",
        "isdn_13": "9782048742975",
        "isdn_10": "2048742971",
        "language": "english",
        "title": "The Raven",
    }


@pytest.mark.django_db
def test_books_retrieve_number_of_queries(retrieve_books, book, django_assert_num_queries):
    with django_assert_num_queries(1):
        retrieve_books(book.isdn_13)


@pytest.mark.django_db
def test_books_update_status_code(update_books, book):
    response = update_books(book.isdn_13, {})
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_books_update_data(update_books, book):
    response = update_books(book.isdn_13, {})
    assert response.json() == {
        "author": 1,
        "date_published": "2024-09-04",
        "isdn_13": "9782048742975",
        "isdn_10": "2048742971",
        "language": "english",
        "title": "The Raven",
    }


@pytest.mark.django_db
def test_books_update_number_of_queries(update_books, book, django_assert_num_queries):
    with django_assert_num_queries(2):
        update_books(book.isdn_13, {})


@pytest.mark.django_db
def test_books_status_code(delete_books, book):
    response = delete_books(book.isdn_13)
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_books_delete_number_of_queries(delete_books, book, django_assert_num_queries):
    with django_assert_num_queries(2):
        delete_books(book.isdn_13)
