from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import BannerImage, ContactInfo, OurClients, LegalDocument
from .serializers import (
    BannerImageSerializer,
    ContactInfoSerializer,
    OurClientsSerializer,
    LegalDocumentSerializer,
)


class HomePageTemplateView(TemplateView):
    template_name = "home/index.html"


class BannerImageViewSet(viewsets.ModelViewSet):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class OurClientsViewSet(viewsets.ModelViewSet):
    queryset = OurClients.objects.all()
    serializer_class = OurClientsSerializer


class LegalDocumentViewSet(viewsets.ModelViewSet):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer
