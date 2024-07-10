from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BannerImageViewSet,
    ContactInfoViewSet,
    AboutUsViewSet,
    OurClientsViewSet,
    LegalDocumentViewSet,
)

router = DefaultRouter()
router.register("banners", BannerImageViewSet)
router.register("contact-info", ContactInfoViewSet)
router.register("about-us", AboutUsViewSet)
router.register("our-clients", OurClientsViewSet)
router.register("legal-documents", LegalDocumentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
