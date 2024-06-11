from rest_framework import serializers
from .models import (
    PlantCategory,
    Plant,
    PlantImage,
    PlanterCategory,
    Planter,
    PlanterImage,
    ServiceCategory,
    ServiceType,
    ServiceTypeFeature,
    Service,
    Tag,
)


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = ["id", "name", "description", "image"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ["id", "plant", "image", "short_description"]


class PlantSerializer(serializers.ModelSerializer):
    category = PlantCategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    images = PlantImageSerializer(source="plantimage_set", many=True, read_only=True)

    class Meta:
        model = Plant
        fields = [
            "id",
            "title",
            "category",
            "indoor_or_outdoor",
            "size",
            "description",
            "care_instructions",
            "tags",
            "created_at",
            "images",
        ]


class PlanterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterCategory
        fields = ["id", "name", "description", "image"]


class PlanterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterImage
        fields = ["id", "planter", "image", "short_description"]


class PlanterSerializer(serializers.ModelSerializer):
    category = PlanterCategorySerializer()
    images = PlanterImageSerializer(
        source="planterimage_set", many=True, read_only=True
    )

    class Meta:
        model = Planter
        fields = ["id", "model", "size", "description", "color", "category", "images"]


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "title", "description", "image"]


class ServiceTypeFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTypeFeature
        fields = ["id", "title"]


class ServiceTypeSerializer(serializers.ModelSerializer):
    service_type_features = ServiceTypeFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceType
        fields = [
            "id",
            "title",
            "description",
            "image",
            "budget_range",
            "service_type_features",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    type = ServiceTypeSerializer(read_only=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "description",
            "image",
            "budget_range",
            "category",
            "type",
        ]
