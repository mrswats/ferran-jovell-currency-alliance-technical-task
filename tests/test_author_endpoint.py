from http import HTTPStatus
from typing import Any

import pytest
from rest_framework.reverse import reverse


@pytest.fixture
def author_data():
    return {
        "name": "H. P. Lovecraft",
        "birth_date": "1890-08-20",
        "nationality": "american",
    }


@pytest.fixture
def authors_url():
    return reverse("api:authors-list")


@pytest.fixture
def authors_detail_url():
    def _(author_id: str) -> str:
        return reverse("api:authors-detail", kwargs={"pk": author_id})

    return _


@pytest.fixture
def list_authors(client, authors_url):
    def _():
        return client.get(authors_url)

    return _


@pytest.fixture
def retrieve_authors(client, authors_detail_url):
    def _(author_id: str):
        return client.get(authors_detail_url(author_id))

    return _


@pytest.fixture
def create_authors(client, authors_url):
    def _(data: dict[str, Any]):
        return client.post(authors_url, data=data)

    return _


@pytest.fixture
def update_authors(client, authors_detail_url):
    def _(author_id: str, data: dict[str, Any]):
        return client.patch(authors_detail_url(author_id), data=data)

    return _


@pytest.fixture
def delete_authors(client, authors_detail_url):
    def _(author_id: str):
        return client.delete(authors_detail_url(author_id))

    return _


def test_authors_url(authors_url):
    assert authors_url == "/api/authors/"


def test_authors_detail_url(authors_detail_url):
    assert authors_detail_url("author-id") == "/api/authors/author-id/"


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
            "birth_date": "1809-01-19",
            "id": 1,
            "name": "Edgar Allan Poe",
            "nationality": "american",
        }
    ]


@pytest.mark.django_db
def test_authors_list_data_number_of_queries(list_authors, django_assert_num_queries):
    with django_assert_num_queries(1):
        list_authors()


@pytest.mark.django_db
def test_authors_retrieve_status_code(retrieve_authors, author):
    response = retrieve_authors(author.pk)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_authors_no_author_status_code(retrieve_authors):
    response = retrieve_authors("foo")
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.django_db
def test_authors_retrieve_data(retrieve_authors, author):
    response = retrieve_authors(author.pk)
    assert response.json() == {
        "birth_date": "1809-01-19",
        "id": 1,
        "name": "Edgar Allan Poe",
        "nationality": "american",
    }


@pytest.mark.django_db
def test_authors__retrieve_data_number_of_queries(
    retrieve_authors, author, django_assert_num_queries
):
    with django_assert_num_queries(1):
        retrieve_authors(author.pk)


@pytest.mark.django_db
def test_authors_create_status_code(create_authors, author_data):
    response = create_authors(author_data)
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db
def test_authors_create_data(create_authors, author_data):
    response = create_authors(author_data)
    assert response.json() == {
        "id": 1,
        **author_data,
    }


@pytest.mark.django_db
def test_authors_create_number_of_queries(
    create_authors, author_data, django_assert_num_queries
):
    with django_assert_num_queries(1):
        create_authors(author_data)


@pytest.mark.django_db
def test_authors_update_status_code(update_authors, author):
    response = update_authors(author.pk, {})
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    "key, value",
    {
        ("birth_date", "1808-01-19"),
        ("name", "Poe"),
        ("nationality", "english"),
    },
)
@pytest.mark.django_db
def test_authors_update_data(update_authors, author, key, value):
    response = update_authors(author.pk, {key: value})
    assert response.json().get(key) == value


@pytest.mark.django_db
def test_authors_update_number_of_queries(
    update_authors, author, django_assert_num_queries
):
    with django_assert_num_queries(2):
        update_authors(author.pk, {})


@pytest.mark.django_db
def test_authors_delete_status_code(delete_authors, author):
    response = delete_authors(author.pk)
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_authors_delete_number_of_queries(
    delete_authors, author, django_assert_num_queries
):
    with django_assert_num_queries(3):
        delete_authors(author.pk)
