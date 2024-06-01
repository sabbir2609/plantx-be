from rest_framework import viewsets
from .models import DesignCategory, Design, DesignImage
from .serializers import (
    DesignCategorySerializer,
    DesignSerializer,
    DesignImageSerializer,
)


class DesignCategoryViewSet(viewsets.ModelViewSet):
    queryset = DesignCategory.objects.all()
    serializer_class = DesignCategorySerializer


class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    serializer_class = DesignSerializer


class DesignImageViewSet(viewsets.ModelViewSet):
    queryset = DesignImage.objects.all()
    serializer_class = DesignImageSerializer
