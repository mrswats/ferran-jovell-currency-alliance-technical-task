from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.fixture
def authors_url():
    return reverse("api:authors-list")


@pytest.fixture
def list_authors(client, authors_url):
    def _():
        return client.get(authors_url)

    return _


def test_authors_url(authors_url):
    assert authors_url == "/api/authors/"


@pytest.mark.django_db
def test_authors_status_code(list_authors):
    response = list_authors()
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_authors_empty_data(list_authors):
    response = list_authors()
    assert response.json()["results"] == []


@pytest.mark.django_db
def test_authors_data(list_authors, author):
    response = list_authors()
    assert response.json()["results"] == [
        {
            "id": 1,
            "name": "Edgar Allan Poe",
        }
    ]


@pytest.mark.django_db
def test_authors_data_number_of_queries(list_authors, django_assert_num_queries):
    with django_assert_num_queries(1):
        list_authors()
