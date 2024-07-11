from django.contrib import admin
from .models import (
    PlantCategory,
    Plant,
    PlantImage,
    PlanterCategory,
    PlanterFeatures,
    Planter,
    PlanterImage,
    ServiceCategory,
    ServiceImage,
    Service,
    PlantFeatures,
    Ideas,
    Testimonial,
    Team,
)

from ckeditor.widgets import CKEditorWidget
from django.db import models


@admin.register(PlantCategory)
class PlantCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1


@admin.register(PlantFeatures)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    inlines = [PlantImageInline]
    list_display = ("title", "indoor_or_outdoor", "size", "category")
    search_fields = ("category__name", "indoor_or_outdoor", "size")
    list_filter = ("category", "indoor_or_outdoor", "size")
    filter_horizontal = ("features",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "category",
                    "indoor_or_outdoor",
                    "size",
                    "description",
                    "care_instructions",
                    "features",
                    "tags",
                )
            },
        ),
    )
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}
    list_per_page = 10


class PlanterImageInline(admin.TabularInline):
    model = PlanterImage
    extra = 1


@admin.register(PlanterFeatures)
class PlanterFeaturesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Planter)
class PlanterAdmin(admin.ModelAdmin):
    inlines = [PlanterImageInline]
    list_display = ("model", "size", "color", "category")
    search_fields = ("model", "size", "color")
    list_filter = ("category", "size", "color")
    filter_horizontal = ("features",)
    list_per_page = 10
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


@admin.register(PlanterCategory)
class PlanterCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "type",
    )
    search_fields = ("title",)


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "budget_range",
    )
    search_fields = ("title", "budget_range")
    list_filter = ("categories",)
    filter_horizontal = ("categories",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "categories",
                    "description",
                    "budget_range",
                    "tags",
                )
            },
        ),
    )
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}
    list_per_page = 10
    inlines = [ServiceImageInline]


@admin.register(Ideas)
class IdeasAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "image",
                    "tags",
                )
            },
        ),
    )

    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}
    list_per_page = 10


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    list_per_page = 10


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    list_per_page = 10
