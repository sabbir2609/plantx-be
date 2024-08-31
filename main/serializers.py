from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from tags.models import TaggedItem
from tags.serializers import TaggedItemSerializer
from zone.models import ProductZone
from zone.serializers import ProductZoneSerializer
from django.contrib.auth import get_user_model

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
    Event,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class LimitedCustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = [
            "id",
            "user",
            "image",
        ]


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
    zones = serializers.SerializerMethodField()

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
            "zones",
            "tags",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = instance.category.name
        return response

    def get_images(self, obj):
        return ImageSerializer(obj.images.all(), many=True).data

    def get_features(self, obj):
        return FeatureSerializer(obj.features.all(), many=True).data

    def get_zones(self, obj):
        return ProductZoneSerializer(obj.zones.all(), many=True).data

    def get_tags(self, obj):
        return TaggedItemSerializer(obj.tags.all(), many=True).data


class PlantListSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    promotion = PromotionSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "slug",
            "sku",
            "image",
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

    def get_features(self, obj):
        features = obj.prefetched_features[:2]
        return FeatureSerializer(features, many=True).data

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.prefetched_images:
            first_image = obj.prefetched_images[0]
            image_url = first_image.image.url  # This is a relative URL
            if request is not None:
                return request.build_absolute_uri(image_url)  # Converts to absolute URL
            return image_url  # Fallback to relative URL if no request in context
        return None


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
    features = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    promotion = PromotionSerializer(many=True, read_only=True)

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
            "image",
            "features",
            "promotion",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["category"] = instance.category.name
        return response

    def get_features(self, obj):
        features = obj.prefetched_features[:2]
        return FeatureSerializer(features, many=True).data

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.prefetched_images:
            first_image = obj.prefetched_images[0]
            image_url = first_image.image.url  # This is a relative URL
            if request is not None:
                return request.build_absolute_uri(image_url)
            return image_url
        return None


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


# TODO: add planting accessories serializers
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


class ServiceCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = [
            "id",
            "title",
            "slug",
            "type",
            "image",
        ]


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = [
            "id",
            "title",
            "slug",
            "type",
            "description",
            "image",
        ]


class LimitedServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = [
            "id",
            "type",
            "title",
            "slug",
        ]


class ServiceListSerializer(serializers.ModelSerializer):
    categories = LimitedServiceCategorySerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "slug",
            "categories",
            "description",
            "image",
        ]

    def get_image(self, service):
        # Get the first image associated with the service
        image = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Service),
            object_id=service.id,
        ).first()
        return image.image.url if image and image.image else None


class ServiceSerializer(serializers.ModelSerializer):
    categories = LimitedServiceCategorySerializer(many=True, read_only=True)
    images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "slug",
            "categories",
            "description",
            "images",
            "tags",
        ]

    def get_images(self, service):
        images = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Service),
            object_id=service.id,
        )
        return ImageSerializer(images, many=True).data

    def get_tags(self, service):
        tags = TaggedItem.objects.filter(
            content_type=ContentType.objects.get_for_model(Service),
            object_id=service.id,
        )
        return TaggedItemSerializer(tags, many=True).data


class IdeasListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = [
            "id",
            "title",
            "slug",
            "image",
        ]


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "image",
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    customer = LimitedCustomerSerializer()

    class Meta:
        model = Testimonial
        fields = [
            "id",
            "customer",
            "slug",
            "content",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["customer"] = (
            f"{instance.customer.user.first_name} {instance.customer.user.last_name}"
        )
        response["image"] = (
            instance.customer.image.url if instance.customer.image else None
        )
        return response


class TeamContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamContact
        fields = [
            "id",
            "social_media_name",
            "social_media_link",
        ]


class TeamListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Team
        fields = [
            "id",
            "serial",
            "user",
            "slug",
            "image",
            "position",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = f"{instance.user.first_name} {instance.user.last_name}"
        return response


class TeamSerializer(serializers.ModelSerializer):
    contacts = TeamContactSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Team
        fields = [
            "id",
            "serial",
            "user",
            "slug",
            "position",
            "bio",
            "contacts",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = f"{instance.user.first_name} {instance.user.last_name}"
        return response


class ProjectsListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "slug",
            "client",
            "year",
            "image",
        ]

    def get_image(self, project):
        # Get the first image associated with the project
        image = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Projects),
            object_id=project.id,
        ).first()
        return image.image.url if image and image.image else None


class ProjectsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    categories = LimitedServiceCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "slug",
            "categories",
            "client",
            "year",
            "description",
            "images",
        ]

    def get_images(self, project):
        images = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(Projects),
            object_id=project.id,
        )
        return ImageSerializer(images, many=True).data


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "slug",
            "date",
            "location",
            "image",
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "slug",
            "date",
            "location",
            "description",
            "image",
        ]
