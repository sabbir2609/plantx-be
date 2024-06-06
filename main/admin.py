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
    Service,
    Tag,
)


class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    inlines = [PlantImageInline]
    list_display = ("category", "indoor_or_outdoor", "size", "created_at")
    search_fields = ("category__name", "indoor_or_outdoor", "size")
    list_filter = ("category", "indoor_or_outdoor", "size")
    filter_horizontal = ("tags",)
    fieldsets = (
        (
            None,
            {
                "fields": (
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


@admin.register(PlantCategory)
class PlantCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class PlanterImageInline(admin.TabularInline):
    model = PlanterImage
    extra = 1


@admin.register(Planter)
class PlanterAdmin(admin.ModelAdmin):
    inlines = [PlanterImageInline]
    list_display = ("model", "size", "color", "category")
    search_fields = ("model", "size", "color")
    list_filter = ("category", "size", "color")


@admin.register(PlanterCategory)
class PlanterCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "budget_range")
    search_fields = ("title", "budget_range")


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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
