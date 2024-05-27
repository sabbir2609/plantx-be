from django.urls import path
from .views import (
    HomePageView,
    PlantListView,
    PlantDetailView,
    CategoryListView,
    CategoryDetailView,
)

app_name = "main"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("plants/", PlantListView.as_view(), name="plant-list"),
    path("plants/<str:slug>/", PlantDetailView.as_view(), name="plant-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<str:slug>/", CategoryDetailView.as_view(), name="category-detail"
    ),
]
