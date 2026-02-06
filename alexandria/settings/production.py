import os

from alexandria.settings.base import *  # noqa: F401,F403


DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS: list[str] = os.getenv("ALLOWED_HOSTS", "").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT", "5432"),
    }
}
