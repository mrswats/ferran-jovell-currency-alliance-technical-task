from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("alexandria.health.urls")),
    path("", include("alexandria.shelves.urls", namespace="api")),
    path("docs/", include("alexandria.docs", namespace="docs")),
]
