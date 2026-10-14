
from rest_framework.routers import DefaultRouter

from .api_views import AuthorViewSet, BookViewSet, TagViewSet


router = DefaultRouter()

router.register("authors", AuthorViewSet)
router.register("tags", TagViewSet)
router.register("books", BookViewSet)

urlpatterns = router.urls
