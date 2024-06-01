from rest_framework import serializers
from .models import DesignCategory, Design, DesignImage


class DesignCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignCategory
        fields = "__all__"


class DesignImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignImage
        fields = "__all__"


class DesignSerializer(serializers.ModelSerializer):
    images = DesignImageSerializer(many=True, read_only=True)

    class Meta:
        model = Design
        fields = "__all__"
