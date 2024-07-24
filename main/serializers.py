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
    Service,
    ServiceImage,
    Ideas,
    Testimonial,
    Team,
    TeamContact,
    Projects,
    ProjectImage,
)


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = ["id", "name", "description", "image"]


class PlantFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantFeatures
        fields = ["id", "name"]


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ["id", "plant", "image", "short_description"]


class PlantSerializer(serializers.ModelSerializer):
    category = PlantCategorySerializer()
    features = PlantFeaturesSerializer(many=True)
    images = PlantImageSerializer(many=True, source="plantimage_set", read_only=True)

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
            "images",
            "created_at",
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


class PlanterSerializer(serializers.ModelSerializer):
    category = PlanterCategorySerializer()
    features = PlanterFeaturesSerializer(many=True)
    images = PlanterImageSerializer(
        many=True, source="planterimage_set", read_only=True
    )

    class Meta:
        model = Planter
        fields = [
            "id",
            "model",
            "category",
            "size",
            "description",
            "features",
            "color",
            "is_custom",
            "images",
        ]


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "serial", "type", "title", "description", "image"]


class LimitedServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "title", "type"]


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ["id", "service", "image", "short_description"]


class ServiceSerializer(serializers.ModelSerializer):
    categories = ServiceCategorySerializer(many=True)
    images = ServiceImageSerializer(
        many=True, source="serviceimage_set", read_only=True
    )

    class Meta:
        model = Service
        fields = ["id", "title", "description", "categories", "images"]


class LimitedServiceSerializer(serializers.ModelSerializer):
    categories = LimitedServiceCategorySerializer(read_only=True, many=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "image",
            "categories",
        ]

    def get_image(self, obj):
        request = self.context.get("request")
        first_image_instance = obj.serviceimage_set.first()
        if first_image_instance:
            image_url = first_image_instance.image.url
            return request.build_absolute_uri(image_url) if request else image_url
        return None


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ["id", "title", "description", "image", "created_at"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["id", "name", "image", "content", "created_at"]


class TeamContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamContact
        fields = ["id", "team", "social_media_name", "social_media_link"]


class TeamSerializer(serializers.ModelSerializer):
    contacts = TeamContactSerializer(
        many=True, source="teamcontact_set", read_only=True
    )

    class Meta:
        model = Team
        fields = [
            "id",
            "serial",
            "name",
            "position",
            "image",
            "bio",
            "created_at",
            "contacts",
        ]


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "project", "image", "short_description"]


class ProjectsSerializer(serializers.ModelSerializer):
    categories = ServiceCategorySerializer(many=True)
    images = ProjectImageSerializer(
        many=True, source="projectimage_set", read_only=True
    )

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "categories",
            "description",
            "client",
            "year",
            "created_at",
            "images",
        ]
