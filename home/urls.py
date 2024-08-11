from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BannerImageViewSet,
    ContactInfoViewSet,
    OurClientsViewSet,
    LegalDocumentViewSet,
    ContactMessageViewSet,
)

router = DefaultRouter()
router.register("banners", BannerImageViewSet, basename="banner-image")
router.register("contact-info", ContactInfoViewSet, basename="contact-info")
router.register("our-clients", OurClientsViewSet, basename="our-clients")
router.register("legal-documents", LegalDocumentViewSet, basename="legal-document")
router.register("contact", ContactMessageViewSet, basename="contact-message")

urlpatterns = [
    path("", include(router.urls)),
]
