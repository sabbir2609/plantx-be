# from django.urls import path, include
# from rest_framework_nested import routers
# from .views import (
#     PlantCategoryViewSet,
#     PlantViewSet,
#     PlanterCategoryViewSet,
#     PlanterViewSet,
#     ServiceCategoryViewSet,
#     ServiceViewSet,
#     IdeasViewSet,
#     TestimonialViewSet,
#     TeamViewSet,
#     ProjectsViewSet,
# )

# app_name = "main"

# # the root router
# router = routers.DefaultRouter()

# router.register("plant_categories", PlantCategoryViewSet, basename="plantcategory")
# router.register("plants", PlantViewSet, basename="plant")
# plant_categories_router = routers.NestedDefaultRouter(
#     router, "plant_categories", lookup="plant_category"
# )
# plant_categories_router.register(
#     "plants", PlantViewSet, basename="plant-category-plants"
# )

# router.register(
#     "planter_categories", PlanterCategoryViewSet, basename="plantercategory"
# )
# router.register("planters", PlanterViewSet, basename="planter")

# planter_categories_router = routers.NestedDefaultRouter(
#     router, "planter_categories", lookup="planter_category"
# )
# planter_categories_router.register(
#     "planters", PlanterViewSet, basename="planter-category-planters"
# )


# router.register(
#     "service_categories", ServiceCategoryViewSet, basename="servicecategory"
# )

# router.register("services", ServiceViewSet, basename="services")

# service_categories_router = routers.NestedDefaultRouter(
#     router, "service_categories", lookup="service_categories"
# )
# service_categories_router.register(
#     "services", ServiceViewSet, basename="service-categories-services"
# )

# router.register("ideas", IdeasViewSet, basename="ideas")

# router.register("testimonials", TestimonialViewSet, basename="testimonials")
# router.register("team", TeamViewSet, basename="team")

# router.register("projects", ProjectsViewSet, basename="projects")

# urlpatterns = [
#     path("", include(router.urls)),
#     path("", include(plant_categories_router.urls)),
#     path("", include(planter_categories_router.urls)),
#     path("", include(service_categories_router.urls)),
# ]


urlpatterns = []
