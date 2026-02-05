# Alexandria project for Currency Alliance

This is my implementation for the technical test for the selection process of currency alliance.

## Assumptions

For this project, I assumed a few things about the project:

* I used Django and Django Rest Framework to implement the solution.
* Keeping it simple: I did not complicate myself with much more than the bare CRUD basics.
* Used SQLite for development and PostgreSQL for the "deployment" (with docker-compose).
* There are hard coded credentials given that this is just a technical test.
  For real life project, these would have to be injected via the environment or
  a secrets file or some other way.
* The data model is simple but it is enough to highlight the relationship between Authors and Books.
* The ISBN13 has been used as a unique identifier for books, making it unique
  to ensure data congruency and avoid collisions.
* This same ISBN13 has been used, then, as the key for fetching books from the API.
* For the authors, the primary database key is used. Some sort of unique
  identifier could be used instead of the database index to avoid leaking
  database internal details.
* THe RESTful conventions have been used: plural names and meaningful verbs for each of the CRUD actions.
* Using pre-commit for linting and formatting as well as mypy on strict mode for checking types.
* Full suite of tests for the two endpoints using pytest instead of the builtin django unittest.
* Using python 3.14 as it is the latest release. Using Django 6.0 as it is the latest release.
* Implemented CI for tests, types (mypy) and pre-commit.
* Added an OpenAPI Spec throught DRF Spectacular for an easy to use auto documentation tool.

## Virtual Environment

Create a virtual Environment

```
virtualenv .venv -p pytthon 3.14
source .venv/bin/activate
```

## Tests

Using pytest for Tests

```
python -m pytest
```

## Formatting and Linting

Using pre-commit for linting and formatting

```
pre-commit install
pre-commit run --all-files
```
