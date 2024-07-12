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
    ProjectImage,
    Projects,
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
            "categories",
            "tags",
        ]


class LimitedServiceSerializer(serializers.ModelSerializer):
    categories = LimitedServiceCategorySerializer(read_only=True, many=True)
    tags = TagListSerializerField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "image",
            "categories",
            "tags",
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        first_image_instance = obj.serviceimage_set.first()
        if first_image_instance:
            image_url = first_image_instance.image.url
            return request.build_absolute_uri(image_url) if request else image_url
        return None


class IdeasSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Ideas
        fields = ["id", "title", "description", "image", "tags", "created_at"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "name", "image", "content"]


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "short_description"]


class ProjectsSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "categories",
            "description",
            "client",
            "year",
            "tags",
            "images",
        ]
