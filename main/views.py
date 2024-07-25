# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from .pagination import DefaultPagination

# from .models import (
#     PlantCategory,
#     Plant,
#     PlanterCategory,
#     Planter,
#     ServiceCategory,
#     Service,
#     Ideas,
#     Testimonial,
#     Team,
#     Projects,
# )
# from .serializers import (
#     PlantCategorySerializer,
#     PlantSerializer,
#     LimitedPlantSerializer,
#     PlanterCategorySerializer,
#     PlanterSerializer,
#     LimitedPlanterSerializer,
#     ServiceCategorySerializer,
#     ServiceSerializer,
#     LimitedServiceSerializer,
#     IdeasSerializer,
#     TestimonialSerializer,
#     TeamSerializer,
#     ProjectsSerializer,
# )


# class PlantCategoryViewSet(viewsets.ModelViewSet):
#     queryset = PlantCategory.objects.all()
#     serializer_class = PlantCategorySerializer


# class PlantViewSet(viewsets.ModelViewSet):
#     queryset = Plant.objects.all()
#     pagination_class = DefaultPagination

#     def get_serializer_class(self):
#         if self.action == "list":
#             return LimitedPlantSerializer
#         return PlantSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         plant_category_pk = self.kwargs.get("plant_category_pk")
#         if plant_category_pk:
#             queryset = queryset.filter(category_id=plant_category_pk)
#         return queryset

#     @action(detail=False, url_path="indoor")
#     def indoor(self, request, plant_category_pk=None):
#         queryset = self.get_queryset().filter(location_type="Indoor")
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     @action(detail=False, url_path="outdoor")
#     def outdoor(self, request, plant_category_pk=None):
#         queryset = self.get_queryset().filter(location_type="Outdoor")
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# class PlanterCategoryViewSet(viewsets.ModelViewSet):
#     queryset = PlanterCategory.objects.all()
#     serializer_class = PlanterCategorySerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         planter_category_pk = self.kwargs.get("planter_category_pk")
#         if planter_category_pk:
#             queryset = queryset.filter(category_id=planter_category_pk)
#         return queryset


# class PlanterViewSet(viewsets.ModelViewSet):
#     queryset = Planter.objects.all()
#     pagination_class = DefaultPagination

#     def get_serializer_class(self):
#         if self.action == "list":
#             return LimitedPlanterSerializer
#         return PlanterSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         planter_category_pk = self.kwargs.get("planter_category_pk")
#         if planter_category_pk:
#             queryset = queryset.filter(category_id=planter_category_pk)
#         return queryset

#     @action(detail=False, url_path="custom")
#     def custom(self, request, planter_category_pk=None):
#         queryset = self.get_queryset().filter(is_custom=True)
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     @action(detail=False, url_path="featured")
#     def featured(self, request, planter_category_pk=None):
#         queryset = self.get_queryset().filter(tags__name__in=["featured"])
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# class ServiceCategoryViewSet(viewsets.ModelViewSet):
#     queryset = ServiceCategory.objects.all()
#     serializer_class = ServiceCategorySerializer

#     @action(detail=False, url_path="commercial")
#     def commercial(self, request):
#         queryset = self.get_queryset().filter(type__iexact="Commercial")
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     @action(detail=False, url_path="residential")
#     def residential(self, request):
#         queryset = self.get_queryset().filter(type__iexact="Residential")
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# class ServiceViewSet(viewsets.ModelViewSet):
#     queryset = Service.objects.all()
#     pagination_class = DefaultPagination

#     def get_serializer_class(self):
#         print(f"Current action: {self.action}")  # Debugging line
#         if self.action == "list":
#             return LimitedServiceSerializer
#         return ServiceSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         service_category_pk = self.kwargs.get("service_categories_pk")
#         if service_category_pk:
#             queryset = queryset.filter(categories__pk=service_category_pk)
#         return queryset


# class IdeasViewSet(viewsets.ModelViewSet):
#     queryset = Ideas.objects.all()
#     serializer_class = IdeasSerializer

#     @action(detail=False, url_path="featured")
#     def featured(self, request):
#         queryset = self.get_queryset().filter(tags__name__in=["featured"])
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# class TestimonialViewSet(viewsets.ModelViewSet):
#     queryset = Testimonial.objects.all()
#     serializer_class = TestimonialSerializer


# class TeamViewSet(viewsets.ModelViewSet):
#     queryset = Team.objects.all()
#     serializer_class = TeamSerializer


# class ProjectsViewSet(viewsets.ModelViewSet):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer
#     pagination_class = DefaultPagination
