from rest_framework_nested import routers
from django.urls import path, include
from .views import PlantCategoryViewSet, PlantViewSet, PlantImageViewSet

app_name = "plant"

router = routers.DefaultRouter()
router.register(r"categories", PlantCategoryViewSet)
router.register(r"plants", PlantViewSet)
router.register(r"images", PlantImageViewSet)

# Nested router for plants under categories
categories_router = routers.NestedDefaultRouter(
    router, r"categories", lookup="category"
)
categories_router.register(r"plants", PlantViewSet, basename="category-plants")

# Nested router for images under plants
plants_router = routers.NestedDefaultRouter(router, r"plants", lookup="plant")
plants_router.register(r"images", PlantImageViewSet, basename="plant-images")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(categories_router.urls)),
    path("", include(plants_router.urls)),
]
