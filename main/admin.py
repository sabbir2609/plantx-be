from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import TabularInline

from .models import (
    PlantCategory,
    Plant,
    PlantImage,
    PlanterCategory,
    PlanterFeatures,
    Planter,
    PlanterImage,
    ProjectImage,
    Projects,
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

from django.utils.html import format_html


@admin.register(PlantCategory)
class PlantCategoryAdmin(ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class PlantImageInline(TabularInline):
    model = PlantImage
    extra = 1
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 150px;"/>'
            )
        return ""


@admin.register(PlantFeatures)
class TagAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Plant)
class PlantAdmin(ModelAdmin):
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


class PlanterImageInline(TabularInline):
    model = PlanterImage
    extra = 1
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 150px;"/>'
            )
        return ""


@admin.register(PlanterFeatures)
class PlanterFeaturesAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Planter)
class PlanterAdmin(ModelAdmin):
    inlines = [PlanterImageInline]
    list_display = ("model", "size", "color", "category")
    search_fields = ("model", "size", "color")
    list_filter = ("category", "size", "color")
    filter_horizontal = ("features",)
    list_per_page = 10
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


@admin.register(PlanterCategory)
class PlanterCategoryAdmin(ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(ModelAdmin):
    list_display = (
        "title",
        "type",
    )
    search_fields = ("title",)


class ServiceImageInline(TabularInline):
    model = ServiceImage
    extra = 1
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 150px;"/>'
            )
        return ""


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
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
                    "tags",
                )
            },
        ),
    )
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}
    list_per_page = 10
    inlines = [ServiceImageInline]


@admin.register(Ideas)
class IdeasAdmin(ModelAdmin):
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
class TestimonialAdmin(ModelAdmin):
    list_display = ("name", "created_at")
    list_per_page = 10
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 150px;"/>'
            )
        return ""


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")
    readonly_fields = ("thumbnail",)

    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 150px;"/>'
            )
        return ""


class ProjectImageInline(TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 150px;"/>'
            )
        return ""


@admin.register(Projects)
class ProjectsAdmin(ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ("title", "client", "year", "created_at")
    search_fields = ("title", "client", "year")
    list_filter = ("year",)
    ordering = ("title",)

    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}
