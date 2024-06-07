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


urlpatterns = [
    path("", include(router.urls)),
    path("", include(plant_categories_router.urls)),
]
