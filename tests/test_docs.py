from http import HTTPStatus

import pytest
from rest_framework.reverse import reverse


@pytest.fixture
def docs_schema_url():
    return reverse("docs:schema")


@pytest.fixture
def docs_url():
    return reverse("docs:html")


def test_docs_html_url(docs_url):
    assert docs_url == "/docs/"


def test_docs_schema_url(docs_schema_url):
    assert docs_schema_url == "/docs/openapi.yaml"


def test_docs_html_status_code(client, docs_url):
    response = client.get(docs_url)
    assert response.status_code == HTTPStatus.OK


def test_docs_schema_status_code(client, docs_schema_url):
    response = client.get(docs_schema_url)
    assert response.status_code == HTTPStatus.OK
