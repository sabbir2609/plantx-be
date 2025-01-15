from rest_framework import serializers
from .models import TrackLinks


class TrackLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackLinks
        fields = "__all__"
