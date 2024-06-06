from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False)
    def indoor(self, request):
        queryset = self.get_queryset().filter(indoor_or_outdoor="Indoor")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def outdoor(self, request):
        queryset = self.get_queryset().filter(indoor_or_outdoor="Outdoor")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
