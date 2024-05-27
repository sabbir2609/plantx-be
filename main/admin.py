from django.contrib import admin
from main.models import Category, Plant, PlantImage, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)
    list_per_page = 20


class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "scientific_name",
        "family",
        "origin",
        "description",
        "care_instructions",
        "light_requirements",
        "water_requirements",
        "temperature_range",
        "humidity",
        "soil_type",
        "toxicity",
    )
    search_fields = (
        "name",
        "category",
        "scientific_name",
        "family",
        "origin",
        "description",
        "care_instructions",
        "light_requirements",
        "water_requirements",
        "temperature_range",
        "humidity",
        "soil_type",
        "toxicity",
    )
    fieldsets = (
        (
            "Plant Information",
            {
                "fields": (
                    "name",
                    "category",
                    "scientific_name",
                    "family",
                    "origin",
                    "light_requirements",
                    "water_requirements",
                    "temperature_range",
                    "humidity",
                    "soil_type",
                    "toxicity",
                )
            },
        ),
        (
            "Description",
            {"fields": ("description",)},
        ),
        (
            "Care Instructions",
            {"fields": ("care_instructions",)},
        ),
    )
    ordering = ("name",)
    list_per_page = 20
    inlines = [PlantImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("plant", "rating", "comment", "created_at")
    search_fields = ("plant", "rating", "comment")
    ordering = ("-created_at",)
    list_per_page = 20
