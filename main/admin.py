from django.contrib import admin
from .models import (
    PlantCategory,
    Plant,
    PlantImage,
    PlanterCategory,
    Planter,
    PlanterImage,
    ServiceCategory,
    ServiceType,
    ServiceTypeFeature,
    Service,
    Tag,
)

from django_ckeditor_5.widgets import CKEditor5Widget
from django.db import models


class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    inlines = [PlantImageInline]
    list_display = ("title", "indoor_or_outdoor", "size", "category")
    search_fields = ("category__name", "indoor_or_outdoor", "size")
    list_filter = ("category", "indoor_or_outdoor", "size")
    filter_horizontal = ("tags",)
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
                    "tags",
                )
            },
        ),
    )
    formfield_overrides = {models.TextField: {"widget": CKEditor5Widget}}
    list_per_page = 10


@admin.register(PlantCategory)
class PlantCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

    formfield_overrides = {models.TextField: {"widget": CKEditor5Widget}}


class PlanterImageInline(admin.TabularInline):
    model = PlanterImage
    extra = 1


@admin.register(Planter)
class PlanterAdmin(admin.ModelAdmin):
    inlines = [PlanterImageInline]
    list_display = ("model", "size", "color", "category")
    search_fields = ("model", "size", "color")
    list_filter = ("category", "size", "color")

    list_per_page = 10

    formfield_overrides = {models.TextField: {"widget": CKEditor5Widget}}


@admin.register(PlanterCategory)
class PlanterCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

    formfield_overrides = {models.TextField: {"widget": CKEditor5Widget}}


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

    formfield_overrides = {models.TextField: {"widget": CKEditor5Widget}}


class ServiceTypeFeatureInline(admin.TabularInline):
    model = ServiceTypeFeature
    extra = 1


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "budget_range")
    search_fields = ("title", "budget_range")
    inlines = [ServiceTypeFeatureInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "budget_range", "category", "type")
    search_fields = ("title", "budget_range")
    list_filter = ("category", "type")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "category",
                    "type",
                    "description",
                    "image",
                    "budget_range",
                )
            },
        ),
    )

    formfield_overrides = {models.TextField: {"widget": CKEditor5Widget}}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
