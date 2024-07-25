from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from unfold.admin import ModelAdmin, TabularInline
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.db.models import Count

from .models import (
    Customer,
    Feature,
    Image,
    Promotion,
    PlantCategory,
    Plant,
    PlanterCategory,
    Planter,
    PlantingAccessoriesCategory,
    PlantingAccessories,
    Projects,
    ServiceCategory,
    Service,
    Ideas,
    Testimonial,
    Team,
    TeamContact,
)


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "membership",
    ]
    search_fields = ("phone",)
    list_editable = ("membership",)
    list_per_page = 10
    autocomplete_fields = ("user",)


class ImageInline(GenericTabularInline, TabularInline):
    model = Image


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ("get_object_name", "image", "content_type", "object_id")
    list_filter = ("content_type",)
    search_fields = ("short_description",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("content_type")

    def get_object_name(self, obj):
        return obj.content_object.name


class FeatureInline(GenericTabularInline, TabularInline):
    model = Feature
    extra = 1


@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    list_display = ("name", "content_type", "get_object_name", "object_id")
    list_filter = ("content_type",)
    search_fields = ("name",)
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("content_type")

    def get_object_name(self, obj):
        return obj.content_object.name


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return [("<10", "Low")]

    def queryset(self, request, queryset):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(Promotion)
class PromotionAdmin(ModelAdmin):
    list_display = ("description", "discount", "created_at")
    search_fields = ("description",)
    list_per_page = 10


@admin.register(PlantCategory)
class PlantCategoryAdmin(ModelAdmin):
    list_display = ("name", "plants_count")
    search_fields = ("name",)

    @admin.display(ordering="plants_count")
    def plants_count(self, plantcategory):
        url = (
            reverse("admin:main_plant_changelist")
            + "?"
            + urlencode({"category__id": str(plantcategory.id)})
        )
        return format_html('<a href="{}">{}</a>', url, plantcategory.plants_count)

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(plants_count=Count("plant", distinct=True))
        )


@admin.register(Plant)
class PlantAdmin(ModelAdmin):
    autocomplete_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ImageInline, FeatureInline]
    list_display = (
        "name",
        "category",
        "sku",
        "location_type",
    )
    search_fields = (
        "name",
        "sku",
    )
    list_filter = (
        "category",
        "location_type",
        "size",
        InventoryFilter,
    )
    filter_horizontal = ("promotion",)
    readonly_fields = ("sku",)
    list_per_page = 10


@admin.register(PlanterCategory)
class PlanterCategoryAdmin(ModelAdmin):
    list_display = ("name", "planters_count")
    search_fields = ("name",)

    @admin.display(ordering="planters_count")
    def planters_count(self, plantercategory):
        url = (
            reverse("admin:main_planter_changelist")
            + "?"
            + urlencode({"category__id": str(plantercategory.id)})
        )
        return format_html('<a href="{}">{}</a>', url, plantercategory.planters_count)

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(planters_count=Count("planter", distinct=True))
        )


@admin.register(Planter)
class PlanterAdmin(ModelAdmin):
    inlines = [ImageInline, FeatureInline]
    list_display = ("name", "category", "sku", "color")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = (
        "name",
        "size",
        "color",
    )
    list_filter = (
        "category",
        "color",
    )
    filter_horizontal = ("promotion",)
    list_per_page = 10


@admin.register(PlantingAccessoriesCategory)
class PlantingAccessoriesCategoryAdmin(ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(PlantingAccessories)
class PlantingAccessoriesAdmin(ModelAdmin):
    inlines = [ImageInline, FeatureInline]
    list_display = ("name", "sku", "category")
    search_fields = (
        "name",
        "sku",
    )
    list_filter = ("category",)
    filter_horizontal = ("promotion",)
    list_per_page = 10


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(ModelAdmin):
    list_display = (
        "title",
        "type",
    )
    search_fields = ("title",)


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
                )
            },
        ),
    )
    list_per_page = 10
    inlines = [ImageInline]


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
                )
            },
        ),
    )
    list_per_page = 10


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("customer", "created_at")
    prepopulated_fields = {"slug": ("customer",)}  # Use 'customer' directly
    autocomplete_fields = ("customer",)
    list_per_page = 10


class TeamContactInline(TabularInline):
    model = TeamContact
    extra = 1


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = ("first_name", "last_name", "position")
    search_fields = ("first_name", "last_name", "position")
    inlines = [TeamContactInline]
    prepopulated_fields = {"slug": ("user",)}


@admin.register(Projects)
class ProjectsAdmin(ModelAdmin):
    inlines = [ImageInline]
    list_display = ("title", "client", "year", "created_at")
    search_fields = ("title", "client", "year")
    list_filter = ("year",)
    ordering = ("title",)
