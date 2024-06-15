from rest_framework import serializers
from .models import (
    PlantCategory,
    Features,
    Plant,
    PlantImage,
    PlanterCategory,
    Planter,
    PlanterImage,
    ServiceCategory,
    ServiceType,
    ServiceTypeFeature,
    Service,
    Ideas,
)
from taggit.serializers import TagListSerializerField, TaggitSerializer


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = ["id", "name", "description", "image"]


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Features
        fields = ["id", "name"]


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ["id", "plant", "image", "short_description"]


class PlantSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = PlantCategorySerializer(read_only=True)
    features = FeaturesSerializer(many=True)
    images = PlantImageSerializer(source="plantimage_set", many=True, read_only=True)
    tags = TagListSerializerField()

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
            "features",
            "created_at",
            "images",
            "tags",
        ]


class PlanterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterCategory
        fields = ["id", "name", "description", "image"]


class PlanterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterImage
        fields = ["id", "planter", "image", "short_description"]


class PlanterSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = PlanterCategorySerializer()
    images = PlanterImageSerializer(
        source="planterimage_set", many=True, read_only=True
    )
    tags = TagListSerializerField()

    class Meta:
        model = Planter
        fields = [
            "id",
            "model",
            "size",
            "description",
            "color",
            "category",
            "images",
            "tags",
        ]


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


class LimitedServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ["id", "title"]


class LimitedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "title"]


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = LimitedServiceSerializer(read_only=True)
    type = LimitedServiceTypeSerializer(read_only=True)
    tags = TagListSerializerField()

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
            "tags",
        ]


class IdeasSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Ideas
        fields = ["id", "title", "description", "image", "tags", "created_at"]
