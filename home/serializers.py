from rest_framework import serializers
from .models import BannerImage, ContactInfo, AboutUs, OurClients, LegalDocument


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"


class OurClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClients
        fields = "__all__"


class LegalDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalDocument
        fields = "__all__"
