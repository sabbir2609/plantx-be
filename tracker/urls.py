from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackLinksViewSet

app_name = "tracker"

router = DefaultRouter()
router.register(r"tracklinks", TrackLinksViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
