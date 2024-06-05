from rest_framework import serializers
from .models import (
    Plant,
    PlantImage,
    Planter,
    PlanterImage,
    InteriorDesignService,
    InteriorDesignServiceImage,
)


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ["id", "image", "plant"]


class PlantSerializer(serializers.ModelSerializer):
    images = PlantImageSerializer(many=True, read_only=True)

    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "plant_type",
            "category",
            "description",
            "care_instructions",
            "is_pet_friendly",
            "benefits",
            "tags",
            "inventory",
            "price",
            "created_at",
            "updated_at",
            "images",
        ]


class PlanterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanterImage
        fields = ["id", "image", "planter"]


class PlanterSerializer(serializers.ModelSerializer):
    images = PlanterImageSerializer(many=True, read_only=True)

    class Meta:
        model = Planter
        fields = [
            "id",
            "model",
            "planter_type",
            "size",
            "color",
            "description",
            "inventory",
            "price",
            "created_at",
            "images",
        ]


class InteriorDesignServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorDesignServiceImage
        fields = ["id", "image", "service"]


class InteriorDesignServiceSerializer(serializers.ModelSerializer):
    images = InteriorDesignServiceImageSerializer(many=True, read_only=True)

    class Meta:
        model = InteriorDesignService
        fields = ["id", "name", "description", "price", "created_at", "images"]
