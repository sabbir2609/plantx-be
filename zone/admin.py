from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Zone, ProductZone


@admin.register(Zone)
class ZoneAdmin(ModelAdmin):
    pass


class ProductZoneInline(TabularInline):
    model = ProductZone
    extra = 1
