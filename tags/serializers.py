from rest_framework import serializers
from .models import Tag, TaggedItem


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "label",
        ]


class TaggedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggedItem
        fields = [
            "id",
            "tag",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["tag"] = instance.tag.label
        return response
