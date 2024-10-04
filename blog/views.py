from rest_framework import viewsets
from .models import Post, Category
from .serializers import (
    PostSerializer,
    PostListSerializer,
    PostCreateSerializer,
    CategorySerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        if self.action == "create":
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        blog_category_slug = self.kwargs.get("category_slug")
        if blog_category_slug:
            queryset = queryset.filter(categories__slug=blog_category_slug)
        return queryset
