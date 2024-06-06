from rest_framework import viewsets
from .models import (
    PlantCategory,
    Plant,
    PlanterCategory,
    Planter,
    ServiceCategory,
    ServiceType,
    Service,
)
from .serializers import (
    PlantCategorySerializer,
    PlantSerializer,
    PlanterCategorySerializer,
    PlanterSerializer,
    ServiceCategorySerializer,
    ServiceTypeSerializer,
    ServiceSerializer,
)


class PlantCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlantCategory.objects.all()
    serializer_class = PlantCategorySerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlanterCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlanterCategory.objects.all()
    serializer_class = PlanterCategorySerializer


class PlanterViewSet(viewsets.ModelViewSet):
    queryset = Planter.objects.all()
    serializer_class = PlanterSerializer


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
