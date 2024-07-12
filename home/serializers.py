from rest_framework import serializers
from .models import BannerImage, ContactInfo, OurClients, LegalDocument


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ["id", "image", "alt_text"]


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ["address", "phone", "email"]


class OurClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClients
        fields = "__all__"


class LegalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDocument
        fields = "__all__"
