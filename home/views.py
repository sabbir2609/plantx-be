from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import (
    BannerImage,
    ContactInfo,
    ContactMessage,
    LegalDocument,
    OurClients,
    Announcement,
)
from .serializers import (
    BannerImageSerializer,
    ContactInfoSerializer,
    ContactMessageSerializer,
    LegalDocumentSerializer,
    OurClientsSerializer,
    AnnouncementSerializer,
)


class HomePageTemplateView(TemplateView):
    template_name = "home/index.html"


class BannerImageViewSet(viewsets.ModelViewSet):
    queryset = BannerImage.objects.all()
    serializer_class = BannerImageSerializer

    @action(detail=False, url_path="small_screen")
    def small_screen(self, request):
        queryset = self.get_queryset().filter(screen_size="Small Screen")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path="large_screen")
    def large_screen(self, request):
        queryset = self.get_queryset().filter(screen_size="Large Screen")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class OurClientsViewSet(viewsets.ModelViewSet):
    queryset = OurClients.objects.all()
    serializer_class = OurClientsSerializer


class LegalDocumentViewSet(viewsets.ModelViewSet):
    queryset = LegalDocument.objects.all()
    serializer_class = LegalDocumentSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
