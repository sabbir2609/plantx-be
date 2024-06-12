from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .pagination import DefaultPagination

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
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        plant_category_pk = self.kwargs.get("plant_category_pk")
        if plant_category_pk:
            queryset = queryset.filter(category_id=plant_category_pk)
        return queryset

    @action(detail=False, url_path="indoor")
    def indoor(self, request, plant_category_pk=None):
        queryset = self.get_queryset().filter(indoor_or_outdoor="Indoor")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path="outdoor")
    def outdoor(self, request, plant_category_pk=None):
        queryset = self.get_queryset().filter(indoor_or_outdoor="Outdoor")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PlanterCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlanterCategory.objects.all()
    serializer_class = PlanterCategorySerializer


class PlanterViewSet(viewsets.ModelViewSet):
    queryset = Planter.objects.all()
    serializer_class = PlanterSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        planter_category_pk = self.kwargs.get("planter_category_pk")
        if planter_category_pk:
            queryset = queryset.filter(category_id=planter_category_pk)
        return queryset

    @action(detail=False, url_path="custom")
    def custom(self, request, planter_category_pk=None):
        queryset = self.get_queryset().filter(is_custom=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = DefaultPagination
