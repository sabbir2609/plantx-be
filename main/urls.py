from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlantViewSet, PlanterViewSet, InteriorDesignServiceViewSet

app_name = "main"

router = DefaultRouter()
router.register(r"plants", PlantViewSet)
router.register(r"planters", PlanterViewSet)
router.register(r"interior-design-services", InteriorDesignServiceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
