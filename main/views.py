from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Plant, Planter, InteriorDesignService
from .serializers import (
    PlantSerializer,
    PlanterSerializer,
    InteriorDesignServiceSerializer,
)


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    @action(detail=True, methods=["get"])
    def indoor(self, request):
        plant = Plant.objects.filter(plant_type="indoor")
        serializer = self.get_serializer(plant, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
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
