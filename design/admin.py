from django.contrib import admin
from design.models import Design, DesignCategory, DesignImage


@admin.register(DesignCategory)
class DesignCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class DesignImageInline(admin.TabularInline):
    model = DesignImage
    extra = 1


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "created", "updated")
    list_filter = ("category",)
    search_fields = ("name", "category__name")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [DesignImageInline]
