from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .pagination import DefaultPagination
from .models import Plant, Planter, InteriorDesignService
from .serializers import (
    PlantListSerializer,
    PlantSerializer,
    PlanterSerializer,
    InteriorDesignServiceSerializer,
)


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    pagination_class = DefaultPagination

    def get_serializer_class(self):
        if self.action == "list":
            return PlantListSerializer
        return PlantSerializer

    @action(detail=False, methods=["get"])
    def indoor(self, request):
        plant = Plant.objects.filter(plant_type="indoor")
        serializer = self.get_serializer(plant, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def outdoor(self, request):
        plant = Plant.objects.filter(plant_type="outdoor")
        serializer = self.get_serializer(plant, many=True)
        return Response(serializer.data)


class PlanterViewSet(viewsets.ModelViewSet):
    queryset = Planter.objects.all()
    serializer_class = PlanterSerializer


class InteriorDesignServiceViewSet(viewsets.ModelViewSet):
    queryset = InteriorDesignService.objects.all()
    serializer_class = InteriorDesignServiceSerializer
