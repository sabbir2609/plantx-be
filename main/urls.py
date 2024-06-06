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

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()


router.register(r"plants", PlantViewSet)

router.register(r"plant-categories", PlantCategoryViewSet)
router.register(r"planter-categories", PlanterCategoryViewSet)
router.register(r"service-categories", ServiceCategoryViewSet)
router.register(r"service-types", ServiceTypeViewSet)

# Create a nested router for plants
plant_router = routers.NestedDefaultRouter(
    router, r"plant-categories", lookup="plant_category"
)
plant_router.register(r"plants", PlantViewSet, basename="plant")

# Create a nested router for plant images
plant_image_router = routers.NestedDefaultRouter(
    plant_router, r"plants", lookup="plant"
)

# Create a nested router for planters
planter_router = routers.NestedDefaultRouter(
    router, r"planter-categories", lookup="planter_category"
)
planter_router.register(r"planters", PlanterViewSet, basename="planter")

# Create a nested router for planter images
planter_image_router = routers.NestedDefaultRouter(
    planter_router, r"planters", lookup="planter"
)

# Create a nested router for services
service_router = routers.NestedDefaultRouter(
    router, r"service-categories", lookup="service_category"
)
service_router.register(r"services", ServiceViewSet, basename="service")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(plant_router.urls)),
    path("", include(plant_image_router.urls)),
    path("", include(planter_router.urls)),
    path("", include(planter_image_router.urls)),
    path("", include(service_router.urls)),
]
