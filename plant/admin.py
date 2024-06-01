from django.contrib import admin
from plant.models import PlantCategory, Plant, PlantImage, Review, ReviewImage


@admin.register(PlantCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    ordering = ("name",)
    list_per_page = 20
    prepopulated_fields = {"slug": ["name"]}


class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
    )
    search_fields = (
        "name",
        "category",
    )
    fieldsets = (
        (
            "Plant Information",
            {
                "fields": (
                    "name",
                    "scientific_name",
                    "slug",
                    "category",
                    "toxicity",
                    "is_pet_safe",
                    "is_air_purifying",
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
        (
            "Tags",
            {"fields": ("tags",)},
        ),
    )
    prepopulated_fields = {"slug": ["name"]}
    ordering = ("name",)
    list_per_page = 20
    inlines = [PlantImageInline]


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("plant", "rating", "comment", "created_at")
    search_fields = ("plant", "rating", "comment")
    ordering = ("-created_at",)
    list_per_page = 20
    inlines = [ReviewImageInline]
