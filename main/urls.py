from django.urls import path, include
from rest_framework_nested import routers
from .views import (
    PlantCategoryViewSet,
    PlantViewSet,
    PlanterCategoryViewSet,
    PlanterViewSet,
    ServiceCategoryViewSet,
    ServiceTypeViewSet,
    ServiceViewSet,
)

app_name = "main"

# the root router
router = routers.DefaultRouter()
router.register("plant_categories", PlantCategoryViewSet, basename="plantcategory")
router.register("plants", PlantViewSet, basename="plant")

plant_categories_router = routers.NestedDefaultRouter(
    router, "plant_categories", lookup="plant_category"
)
plant_categories_router.register(
    "plants", PlantViewSet, basename="plant-category-plants"
)

router.register(
    "planter_categories", PlanterCategoryViewSet, basename="plantercategory"
)
router.register("planters", PlanterViewSet, basename="planter")

planter_categories_router = routers.NestedDefaultRouter(
    router, "planter_categories", lookup="planter_category"
)
planter_categories_router.register(
    "planters", PlanterViewSet, basename="planter-category-planters"
)

router.register(
    "service_categories", ServiceCategoryViewSet, basename="servicecategory"
)
router.register("service_types", ServiceTypeViewSet, basename="servicetype")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(plant_categories_router.urls)),
    path("", include(planter_categories_router.urls)),
]
