from django.contrib import admin
from .models import (
    Plant,
    PlantImage,
    Planter,
    PlanterImage,
    InteriorDesignService,
    InteriorDesignServiceImage,
)


# Inline model for PlantImage
class PlantImageInline(admin.TabularInline):
    model = PlantImage
    extra = 1


# Plant admin
@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "plant_type",
        "category",
        "inventory",
        "price",
    )
    search_fields = ("name", "category")
    list_filter = ("plant_type", "category")
    inlines = [PlantImageInline]
    list_per_page = 10


# Inline model for PlanterImage
class PlanterImageInline(admin.TabularInline):
    model = PlanterImage
    extra = 1


# Planter admin
@admin.register(Planter)
class PlanterAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "planter_type",
        "size",
        "inventory",
        "price",
    )
    search_fields = ("model", "planter_type")
    list_filter = ("planter_type", "size")
    inlines = [PlanterImageInline]
    list_per_page = 10


# Inline model for InteriorDesignServiceImage
class InteriorDesignServiceImageInline(admin.TabularInline):
    model = InteriorDesignServiceImage
    extra = 1


# Interior Design Service admin
@admin.register(InteriorDesignService)
class InteriorDesignServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    search_fields = ("name",)
    inlines = [InteriorDesignServiceImageInline]
