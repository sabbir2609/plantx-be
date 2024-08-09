from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from tags.models import TaggedItem
from tags.serializers import TaggedItemSerializer
from zone.models import ProductZone
from zone.serializers import ProductZoneSerializer

from .models import (
    Customer,
    Feature,
    Ideas,
    Image,
    Plant,
    PlantCategory,
    Planter,
    PlanterCategory,
    PlantingAccessories,
    PlantingAccessoriesCategory,
    Projects,
    Promotion,
    Service,
    ServiceCategory,
    Team,
    TeamContact,
    Testimonial,
)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = [
            "id",
            "description",
            "discount",
        ]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "image",
            "short_description",
        ]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = [
            "id",
            "name",
        ]


class PlantCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = [
            "id",
            "name",
            "slug",
            "image",
        ]


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "image",
        ]


class LimitedPlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = [
            "name",
        ]


class PlantSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    zone = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "sku",
            "category",
            "location_type",
            "size",
            "images",
            "description",
            "care_instructions",
            "promotion",
            "features",
            "zone",
            "tags",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = instance.category.name
        return response

    def get_features(self, plant):
        features = Feature.objects.filter(
            content_type=ContentType.objects.get_for_model(Plant), object_id=plant.id
        )
        return FeatureSerializer(features, many=True).data

    def get_images(self, plant):
        images = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Plant), object_id=plant.id
        )
        return ImageSerializer(images, many=True).data

    def get_tags(self, plant):
        tags = TaggedItem.objects.filter(
            content_type=ContentType.objects.get_for_model(Plant), object_id=plant.id
        )
        return TaggedItemSerializer(tags, many=True).data

    def get_zone(self, plant):
        zones = ProductZone.objects.filter(
            content_type=ContentType.objects.get_for_model(Plant), object_id=plant.id
        )
        return ProductZoneSerializer(zones, many=True).data


class PlantListSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    promotion = PromotionSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "slug",
            "sku",
            "image_url",
            "category",
            "features",
            "promotion",
            "location_type",
            "size",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = instance.category.name

        return response

    def get_features(self, plant):
        features = Feature.objects.filter(
            content_type=ContentType.objects.get_for_model(Plant), object_id=plant.id
        )
        return FeatureSerializer(features, many=True).data

    def get_image_url(self, plant):
        # Get the first image associated with the plant
        image = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Plant),
            object_id=plant.id,
        ).first()
        return image.image.url if image and image.image else None


class PlanterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterCategory
        fields = [
            "id",
            "name",
            "description",
            "image",
        ]


class PlanterCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterCategory
        fields = [
            "id",
            "name",
            "slug",
            "image",
        ]


class LimitedPlanterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterCategory
        fields = [
            "name",
        ]


class PlanterListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    features = serializers.SerializerMethodField()
    category = LimitedPlanterCategorySerializer()

    class Meta:
        model = Planter
        fields = [
            "id",
            "name",
            "slug",
            "sku",
            "category",
            "size",
            "color",
            "is_custom",
            "image_url",
            "features",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = instance.category.name
        return response

    def get_image_url(self, planter):
        # Get the first image associated with the planter
        image = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Planter),
            object_id=planter.id,
        ).first()
        return image.image.url if image and image.image else None

    def get_features(self, planter):
        features = Feature.objects.filter(
            content_type=ContentType.objects.get_for_model(Planter),
            object_id=planter.id,
        )
        return FeatureSerializer(features, many=True).data


class PlanterSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    zone = serializers.SerializerMethodField()

    class Meta:
        model = Planter
        fields = [
            "id",
            "name",
            "sku",
            "category",
            "size",
            "color",
            "is_custom",
            "images",
            "description",
            "features",
            "zone",
            "tags",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = instance.category.name
        return response

    def get_features(self, planter):
        features = Feature.objects.filter(
            content_type=ContentType.objects.get_for_model(Planter),
            object_id=planter.id,
        )
        return FeatureSerializer(features, many=True).data

    def get_images(self, planter):
        images = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Planter),
            object_id=planter.id,
        )
        return ImageSerializer(images, many=True).data

    def get_tags(self, planter):
        tags = TaggedItem.objects.filter(
            content_type=ContentType.objects.get_for_model(Planter),
            object_id=planter.id,
        )
        return TaggedItemSerializer(tags, many=True).data

    def get_zone(self, planter):
        zones = ProductZone.objects.filter(
            content_type=ContentType.objects.get_for_model(Planter),
            object_id=planter.id,
        )
        return ProductZoneSerializer(zones, many=True).data


class PlantingAccessoriesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantingAccessoriesCategory
        fields = "__all__"


class PlantingAccessoriesSerializer(serializers.ModelSerializer):
    tagged_items = TaggedItemSerializer(many=True, read_only=True)
    product_zones = ProductZoneSerializer(many=True, read_only=True)

    class Meta:
        model = PlantingAccessories
        fields = "__all__"


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class LimitedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["id", "name"]


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class TeamContact(serializers.ModelSerializer):
    class Meta:
        model = TeamContact
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    contact = TeamContact(many=True, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
