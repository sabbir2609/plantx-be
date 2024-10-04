from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "image",
            "short_description",
        ]


class LimitedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
        ]


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    categories = LimitedCategorySerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "image",
            "author_name",
            "categories",
            "created_at",
        ]

    def get_author_name(self, obj):
        return obj.author.full_name


class PostListSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    categories = LimitedCategorySerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "author_name",
            "categories",
            "created_at",
        ]

    def get_content(self, obj):
        return obj.content[:109]

    def get_author_name(self, obj):
        return obj.author.full_name


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "slug", "content", "author", "categories"]
