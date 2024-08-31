from django.contrib.contenttypes.models import ContentType
from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from zone.models import ProductZone

from .models import (
    Feature,
    Ideas,
    Image,
    Plant,
    PlantCategory,
    Planter,
    PlanterCategory,
    Projects,
    Service,
    ServiceCategory,
    Team,
    Testimonial,
    Event,
)
from .pagination import DefaultPagination
from .serializers import (
    IdeasListSerializer,
    IdeasSerializer,
    ImageSerializer,
    PlantCategoryListSerializer,
    PlantCategorySerializer,
    PlanterCategoryListSerializer,
    PlanterCategorySerializer,
    PlanterListSerializer,
    PlanterSerializer,
    PlantListSerializer,
    PlantSerializer,
    ProjectsListSerializer,
    ProjectsSerializer,
    ServiceCategoryListSerializer,
    ServiceCategorySerializer,
    ServiceListSerializer,
    ServiceSerializer,
    TeamListSerializer,
    TeamSerializer,
    TestimonialSerializer,
    EventListSerializer,
    EventSerializer,
)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PlantCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlantCategory.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return PlantCategoryListSerializer
        return PlantCategorySerializer


class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    pagination_class = DefaultPagination
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return PlantListSerializer
        return PlantSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        content_type = ContentType.objects.get_for_model(Plant)
        plant_category_slug = self.kwargs.get("plant_category_slug")

        if plant_category_slug:
            queryset = queryset.filter(category__slug=plant_category_slug)

        # Prefetch related
        queryset = queryset.select_related("category").prefetch_related(
            "promotion",
            Prefetch(
                "images",
                queryset=Image.objects.filter(content_type=content_type).order_by("id"),
                to_attr="prefetched_images",
            ),
            Prefetch(
                "features",
                queryset=Feature.objects.filter(content_type=content_type).order_by(
                    "id"
                ),
                to_attr="prefetched_features",
            ),
            Prefetch(
                "zones",
                queryset=ProductZone.objects.filter(content_type=content_type).order_by(
                    "id"
                ),
                to_attr="prefetched_zones",
            ),
        )

        return queryset

    @action(detail=False, url_path="indoor")
    def indoor(self, request, plant_category_slug=None):
        queryset = self.get_queryset().filter(location_type="Indoor")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PlantListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PlantListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path="outdoor")
    def outdoor(self, request, plant_category_slug=None):
        queryset = self.get_queryset().filter(location_type="Outdoor")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PlantListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PlantListSerializer(queryset, many=True)
        return Response(serializer.data)


class PlanterCategoryViewSet(viewsets.ModelViewSet):
    queryset = PlanterCategory.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return PlanterCategoryListSerializer
        return PlanterCategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        planter_category_pk = self.kwargs.get("planter_category_pk")
        if planter_category_pk:
            queryset = queryset.filter(category_slug=planter_category_pk)
        return queryset


class PlanterViewSet(viewsets.ModelViewSet):
    queryset = Planter.objects.all()
    pagination_class = DefaultPagination
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return PlanterListSerializer
        return PlanterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        content_type = ContentType.objects.get_for_model(Planter)

        planter_category_slug = self.kwargs.get("planter_category_slug")

        if planter_category_slug:
            queryset = queryset.filter(category__slug=planter_category_slug)

        # Prefetch related
        queryset = queryset.select_related("category").prefetch_related(
            "promotion",
            Prefetch(
                "images",
                queryset=Image.objects.filter(content_type=content_type).order_by("id"),
                to_attr="prefetched_images",
            ),
            Prefetch(
                "features",
                queryset=Feature.objects.filter(content_type=content_type).order_by(
                    "id"
                ),
                to_attr="prefetched_features",
            ),
            Prefetch(
                "zones",
                queryset=ProductZone.objects.filter(content_type=content_type).order_by(
                    "id"
                ),
                to_attr="prefetched_zones",
            ),
        )

        return queryset

    @action(detail=False, url_path="custom")
    def custom(self, request, planter_category_slug=None):
        queryset = self.get_queryset().filter(is_custom=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PlanterListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PlanterListSerializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=False, url_path="featured")
    # def featured(self, request, planter_category_slug=None):
    #     queryset = self.get_queryset().filter(tags__name__in=["featured"])
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceCategoryListSerializer
        return ServiceCategorySerializer

    @action(detail=False, url_path="commercial")
    def commercial(self, request):
        queryset = self.get_queryset().filter(type__iexact="Commercial")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, url_path="residential")
    def residential(self, request):
        queryset = self.get_queryset().filter(type__iexact="Residential")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    pagination_class = DefaultPagination
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        return ServiceSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     service_category_pk = self.kwargs.get("service_categories_pk")
    #     if service_category_pk:
    #         queryset = queryset.filter(categories__pk=service_category_pk)
    #     return queryset


class IdeasViewSet(viewsets.ModelViewSet):
    queryset = Ideas.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return IdeasListSerializer
        return IdeasSerializer

    @action(detail=False, url_path="featured")
    def featured(self, request):
        queryset = self.get_queryset().filter(is_featured=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = "slug"


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return TeamListSerializer
        return TeamSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    pagination_class = DefaultPagination
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectsListSerializer
        return ProjectsSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    pagination_class = DefaultPagination
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        return EventSerializer
