from rest_framework import serializers
from .models import Zone, ProductZone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"


class ProductZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductZone
        fields = "__all__"
