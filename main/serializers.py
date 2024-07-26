from rest_framework import serializers
from .models import (
    Plant,
    Planter,
    PlantingAccessories,
    Customer,
    Promotion,
    PlantCategory,
    PlanterCategory,
    PlantingAccessoriesCategory,
    Feature,
    Image,
    Ideas,
    Service,
    ServiceCategory,
    Testimonial,
    Team,
    TeamContact,
    Projects,
)
from tags.serializers import TaggedItemSerializer
from zone.serializers import ProductZoneSerializer


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
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):
    tagged_items = TaggedItemSerializer(many=True, read_only=True)
    product_zones = ProductZoneSerializer(many=True, read_only=True)
    promotion = PromotionSerializer(read_only=True, many=True)
    features = FeatureSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    category = PlantCategorySerializer(read_only=True)

    class Meta:
        model = Plant
        fields = "__all__"


class LimitedPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
        ]


class PlanterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterCategory
        fields = "__all__"


class PlanterSerializer(serializers.ModelSerializer):
    tagged_items = TaggedItemSerializer(many=True, read_only=True)
    product_zones = ProductZoneSerializer(many=True, read_only=True)

    class Meta:
        model = Planter
        fields = "__all__"


class LimitedPlanterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planter
        fields = ["id", "name"]


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
