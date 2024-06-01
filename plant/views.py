from rest_framework import viewsets
from .pagination import DefaultPagination
from .models import PlantCategory, Plant, PlantImage
from .serializers import PlantCategorySerializer, PlantSerializer, PlantImageSerializer


class PlantCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    pagination_class = DefaultPagination


class PlantImageViewSet(viewsets.ModelViewSet):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
