from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.templatetags.static import static
from django.db import models
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.contrib.import_export.forms import ExportForm, ImportForm

from tinymce.widgets import TinyMCE

from .models import (
    Customer,
    Feature,
    Ideas,
    Image,
    Plant,
    PlantCategory,
    Planter,
    PlanterCategory,
    PlantingAccessories,
    PlantingAccessoriesCategory,
    Projects,
    Promotion,
    Service,
    ServiceCategory,
    Team,
    TeamContact,
    Testimonial,
)


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = [
        "display_header",
        "phone",
        "membership",
    ]
    search_fields = ("phone",)
    list_editable = ("membership",)
    list_per_page = 10
    autocomplete_fields = ("user",)

    list_filter = ("membership",)

    @display(description="Customer", header=True)
    def display_header(self, instance: Customer):
        image_url = (
            instance.image.url if instance.image else static("images/avatar.jpg")
        )
        return [
            instance.user.full_name,
            None,
            instance.user.last_name,
            {
                "path": image_url,
            },
        ]


class ImageInline(GenericTabularInline, TabularInline):
    model = Image
    extra = 1
    tab = True
    hide_title = True


class FeatureInline(GenericTabularInline, TabularInline):
    model = Feature
    extra = 1
    tab = True
    hide_title = True


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
    prepopulated_fields = {"slug": ("name",)}

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
class PlantAdmin(ModelAdmin, ImportExportModelAdmin):
    autocomplete_fields = [
        "category",
        "promotion",
    ]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ImageInline, FeatureInline]
    list_display = [
        "name",
        "category",
        "sku",
        "inventory",
        "location_type",
    ]
    search_fields = [
        "name",
        "sku",
    ]
    list_filter = (
        "category",
        "location_type",
        "size",
        # InventoryFilter,
    )
    filter_horizontal = ("promotion",)
    readonly_fields = ("sku",)
    list_per_page = 10

    formfield_overrides = {
        models.TextField: {
            "widget": TinyMCE,
        },
    }

    import_form_class = ImportForm
    export_form_class = ExportForm


@admin.register(PlanterCategory)
class PlanterCategoryAdmin(ModelAdmin):
    list_display = ("name", "planters_count")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

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
        "sku",
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
    prepopulated_fields = {"slug": ("name",)}


@admin.register(PlantingAccessories)
class PlantingAccessoriesAdmin(ModelAdmin):
    inlines = [ImageInline, FeatureInline]
    list_display = ("name", "sku", "category")
    prepopulated_fields = {"slug": ("name",)}
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
        "serial",
        "type",
    )
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    list_editable = ("serial",)


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("title",)
    autocomplete_fields = [
        "categories",
    ]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    list_filter = ("categories",)
    filter_horizontal = ("categories",)
    list_per_page = 10
    inlines = [ImageInline]

    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }


@admin.register(Ideas)
class IdeasAdmin(ModelAdmin):
    list_per_page = 10
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("customer", "created_at")
    autocomplete_fields = ("customer",)
    list_per_page = 10


class TeamContactInline(TabularInline):
    model = TeamContact
    extra = 1
    tab = True
    hide_title = True


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = (
        "user",
        "serial",
        "position",
    )
    inlines = [TeamContactInline]
    list_editable = ("serial",)

    fieldsets = (
        (
            "Member",
            {
                "fields": (
                    "user",
                    "slug",
                    "position",
                    "serial",
                    "bio",
                    "image",
                )
            },
        ),
    )


@admin.register(Projects)
class ProjectsAdmin(ModelAdmin):
    inlines = [ImageInline]
    list_display = ("title", "client", "year", "created_at")
    search_fields = ("title", "client", "year")
    list_filter = ("year",)
    ordering = ("title",)
    prepopulated_fields = {"slug": ("title",)}


# @admin.register(Image)
# class ImageAdmin(ModelAdmin):
#     list_display = ("get_object_name", "image", "content_type", "object_id")
#     list_filter = ("content_type",)
#     search_fields = ("short_description",)

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         return queryset.select_related("content_type")

#     def get_object_name(self, obj):
#         return obj.content_object.name


# @admin.register(Feature)
# class FeatureAdmin(ModelAdmin):
#     list_display = ("name", "content_type", "get_object_name", "object_id")
#     list_filter = ("content_type",)
#     search_fields = ("name",)
#     list_per_page = 10

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         return queryset.select_related("content_type")

#     def get_object_name(self, obj):
#         return obj.content_object.name
