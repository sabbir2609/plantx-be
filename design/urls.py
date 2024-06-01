from rest_framework_nested import routers
from django.urls import path, include
from .views import DesignCategoryViewSet, DesignViewSet, DesignImageViewSet

router = routers.DefaultRouter()
router.register(r"design-categories", DesignCategoryViewSet)
router.register(r"designs", DesignViewSet)
router.register(r"design-images", DesignImageViewSet)

# Nested router for designs under design categories
categories_router = routers.NestedDefaultRouter(
    router, r"design-categories", lookup="design_category"
)
categories_router.register(r"designs", DesignViewSet, basename="category-designs")

# Nested router for images under designs
designs_router = routers.NestedDefaultRouter(router, r"designs", lookup="design")
designs_router.register(r"images", DesignImageViewSet, basename="design-images")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(categories_router.urls)),
    path("", include(designs_router.urls)),
]
