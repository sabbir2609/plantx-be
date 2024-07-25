# from rest_framework import serializers
# from .models import (
#     Promotion,
#     PlantCategory,
#     PlantFeatures,
#     Plant,
#     PlantImage,
#     PlanterCategory,
#     PlanterFeatures,
#     Planter,
#     PlanterImage,
#     ServiceCategory,
#     Service,
#     ServiceImage,
#     Ideas,
#     Testimonial,
#     Team,
#     TeamContact,
#     Projects,
#     ProjectImage,
# )


# class PromotionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Promotion
#         fields = ["id", "description", "discount"]


# class PlantCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlantCategory
#         fields = ["id", "name", "description", "image"]


# class PlantFeaturesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlantFeatures
#         fields = ["id", "name"]


# class PlantImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlantImage
#         fields = ["id", "image", "short_description"]


# class PlantSerializer(serializers.ModelSerializer):
#     images = PlantImageSerializer(many=True, source="plantimage_set", read_only=True)

#     class Meta:
#         model = Plant
#         fields = [
#             "id",
#             "name",
#             "images",
#             "slug",
#             "size",
#             "category",
#             "features",
#             "location_type",
#             "description",
#             "care_instructions",
#             "sku",
#             "promotion",
#         ]

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data["category"] = instance.category.name
#         data["features"] = [
#             feature["name"]
#             for feature in PlantFeaturesSerializer(
#                 instance.features.all(), many=True
#             ).data
#         ]
#         data["promotion"] = [promo.description for promo in instance.promotion.all()]

#         data["in_stock"] = instance.inventory > 0
#         return data


# class LimitedPlantSerializer(serializers.ModelSerializer):
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = Plant
#         fields = [
#             "id",
#             "name",
#             "image",
#             "slug",
#             "size",
#             "category",
#             "location_type",
#             "description",
#             "sku",
#         ]

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data["category"] = instance.category.name
#         data["features"] = [
#             feature["name"]
#             for feature in PlantFeaturesSerializer(
#                 instance.features.all(), many=True
#             ).data
#         ][:2]
#         data["promotion"] = [promo.description for promo in instance.promotion.all()][
#             :2
#         ]

#     def get_image(self, obj):
#         request = self.context.get("request")
#         first_image_instance = obj.plantimage_set.first()
#         if first_image_instance:
#             image_url = first_image_instance.image.url
#             return request.build_absolute_uri(image_url) if request else image_url
#         return None


# class PlanterCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlanterCategory
#         fields = ["id", "name", "description", "image"]


# class PlanterFeaturesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlanterFeatures
#         fields = ["id", "name"]


# class PlanterImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PlanterImage
#         fields = ["id", "planter", "image", "short_description"]


# class PlanterSerializer(serializers.ModelSerializer):
#     discounted_price = serializers.SerializerMethodField()
#     price_with_tax = serializers.SerializerMethodField()

#     class Meta:
#         model = Planter
#         fields = [
#             "id",
#             "model",
#             "category",
#             "size",
#             "description",
#             "features",
#             "color",
#             "is_custom",
#             "sku",
#             "inventory",
#             "promotion",
#         ]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation["category"] = instance.category.name
#         representation["features"] = [
#             feature.name for feature in instance.features.all()
#         ]
#         representation["promotion"] = [
#             promo.description for promo in instance.promotion.all()
#         ]
#         return representation


# class LimitedPlanterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Planter
#         fields = ["id", "model"]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation["category"] = instance.category.name
#         representation["features"] = [
#             feature.name for feature in instance.features.all()
#         ][:2]
#         representation["promotion"] = [
#             promo.description for promo in instance.promotion.all()
#         ][:2]
#         return representation


# class ServiceCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceCategory
#         fields = ["id", "serial", "type", "title", "description", "image"]


# class LimitedServiceCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceCategory
#         fields = ["id", "title", "type"]


# class ServiceImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ServiceImage
#         fields = ["id", "service", "image", "short_description"]


# class ServiceSerializer(serializers.ModelSerializer):
#     categories = ServiceCategorySerializer(many=True)
#     images = ServiceImageSerializer(
#         many=True, source="serviceimage_set", read_only=True
#     )

#     class Meta:
#         model = Service
#         fields = ["id", "title", "description", "categories", "images"]


# class LimitedServiceSerializer(serializers.ModelSerializer):
#     categories = LimitedServiceCategorySerializer(read_only=True, many=True)
#     image = serializers.SerializerMethodField()

#     class Meta:
#         model = Service
#         fields = [
#             "id",
#             "title",
#             "image",
#             "categories",
#         ]

#     def get_image(self, obj):
#         request = self.context.get("request")
#         first_image_instance = obj.serviceimage_set.first()
#         if first_image_instance:
#             image_url = first_image_instance.image.url
#             return request.build_absolute_uri(image_url) if request else image_url
#         return None


# class IdeasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ideas
#         fields = ["id", "title", "description", "image", "created_at"]


# class TestimonialSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Testimonial
#         fields = ["id", "name", "image", "content", "created_at"]


# class TeamContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TeamContact
#         fields = ["id", "team", "social_media_name", "social_media_link"]


# class TeamSerializer(serializers.ModelSerializer):
#     contacts = TeamContactSerializer(
#         many=True, source="teamcontact_set", read_only=True
#     )

#     class Meta:
#         model = Team
#         fields = [
#             "id",
#             "serial",
#             "name",
#             "position",
#             "image",
#             "bio",
#             "created_at",
#             "contacts",
#         ]


# class ProjectImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectImage
#         fields = ["id", "project", "image", "short_description"]


# class ProjectsSerializer(serializers.ModelSerializer):
#     categories = ServiceCategorySerializer(many=True)
#     images = ProjectImageSerializer(
#         many=True, source="projectimage_set", read_only=True
#     )

#     class Meta:
#         model = Projects
#         fields = [
#             "id",
#             "title",
#             "categories",
#             "description",
#             "client",
#             "year",
#             "created_at",
#             "images",
#         ]
