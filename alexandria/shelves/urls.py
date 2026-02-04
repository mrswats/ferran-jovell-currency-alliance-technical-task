from rest_framework import routers

from alexandria.shelves import views

router = routers.SimpleRouter()
router.register("authors", views.AuthorViewSet, basename="authors")
router.register("books", views.BookViewSet, basename="books")


urlpatterns = router.urls

app_name = "api"
