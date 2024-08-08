from rest_framework.routers import DefaultRouter
from .views import (
    TagViewSet,
    TaggedItemViewSet,
)

app_name = "tags"

router = DefaultRouter()

router.register(r"tags", TagViewSet)
router.register(r"tagged-items", TaggedItemViewSet)

urlpatterns = router.urls
