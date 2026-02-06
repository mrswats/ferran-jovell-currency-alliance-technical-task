from alexandria.settings.base import *  # noqa: F401,F403

SECRET_KEY = "django-insecure-qhy)z4ko=oa^13ne6d*v5quol+@)b1*dvq52o@-!^pa9ja7ti1"

DEBUG = False

ALLOWED_HOSTS: list[str] = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
