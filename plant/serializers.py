from rest_framework import serializers
from .models import PlantCategory, Plant, PlantImage
from taggit.serializers import TagListSerializerField, TaggitSerializer


class PlantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCategory
        fields = "__all__"


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = "__all__"


class PlantSerializer(TaggitSerializer, serializers.ModelSerializer):
    images = PlantImageSerializer(many=True, read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Plant
        fields = "__all__"
