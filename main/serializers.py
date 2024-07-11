from rest_framework import serializers
from .models import (
    PlantCategory,
    PlantFeatures,
    Plant,
    PlantImage,
    PlanterCategory,
    PlanterFeatures,
    Planter,
    PlanterImage,
    ServiceCategory,
    ServiceImage,
    Service,
    Ideas,
    Testimonial,
    Team,
)
from taggit.serializers import TagListSerializerField, TaggitSerializer


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = ["id", "name", "description", "image"]


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantFeatures
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


class PlanterFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterFeatures
        fields = ["id", "name"]


class PlanterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterImage
        fields = ["id", "planter", "image", "short_description"]


class PlanterSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = PlanterCategorySerializer()
    features = PlanterFeaturesSerializer(many=True)
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
            "short_description",
            "color",
            "category",
            "features",
            "images",
            "tags",
        ]


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "no", "title", "type", "description", "image"]


class LimitedServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "title", "type"]


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ["id", "image", "short_description"]


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    categories = LimitedServiceCategorySerializer(read_only=True, many=True)
    tags = TagListSerializerField()
    images = ServiceImageSerializer(
        source="serviceimage_set", many=True, read_only=True
    )

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "description",
            "images",
            "budget_range",
            "categories",
            "tags",
        ]


class IdeasSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Ideas
        fields = ["id", "title", "description", "image", "tags", "created_at"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
