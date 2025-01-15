from rest_framework import viewsets
from .models import TrackLinks
from .serializers import TrackLinksSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


class TrackLinksViewSet(viewsets.ModelViewSet):
    queryset = TrackLinks.objects.all()
    serializer_class = TrackLinksSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_create(self, serializer):
        # Get IP address from request
        ip_address = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if ip_address:
            ip_address = ip_address.split(",")[0]
        else:
            ip_address = self.request.META.get("REMOTE_ADDR")

        # Save the link with additional data
        serializer.save(
            ip_address=ip_address,
            user_agent=self.request.headers.get("User-Agent"),
            referrer=self.request.META.get("HTTP_REFERER", ""),
        )
