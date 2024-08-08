from rest_framework import serializers
from .models import Zone, ProductZone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = [
            "id",
            "name",
            "description",
        ]


class ProductZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductZone
        fields = [
            "id",
            "zone",
            "available",
            "unit",
            "unit_price",
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["zone"] = instance.zone.name
        return response
