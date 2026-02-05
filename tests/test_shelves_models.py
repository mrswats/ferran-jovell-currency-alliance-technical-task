import pytest


@pytest.mark.django_db
def test_str_author(author):
    assert str(author) == author.name


@pytest.mark.django_db
def test_str_book(book):
    assert str(book) == book.title
