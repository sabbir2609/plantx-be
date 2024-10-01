from rest_framework_nested import routers
from .views import PostViewSet, CategoryViewSet

app_name = "blog"

# Create the base router
router = routers.DefaultRouter()
router.register("posts", PostViewSet, basename="post")
router.register("categories", CategoryViewSet, basename="category")

# Create a nested router for categories and posts
category_router = routers.NestedDefaultRouter(router, "categories", lookup="category")
category_router.register("posts", PostViewSet, basename="category-posts")

# Include both the base and nested routers in urlpatterns
urlpatterns = router.urls + category_router.urls
