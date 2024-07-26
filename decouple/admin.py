from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from main.admin import PlantAdmin, PlanterAdmin, PlantingAccessoriesAdmin, ServiceAdmin
from main.models import Plant, Planter, PlantingAccessories, Service
from tags.models import TaggedItem
from zone.models import ProductZone
from unfold.admin import TabularInline


class TagInline(TabularInline, GenericTabularInline):
    autocomplete_fields = [
        "tag",
    ]
    model = TaggedItem
    extra = 1
    tab = True
    hide_title = True


class ProductZoneInline(TabularInline, GenericTabularInline):
    model = ProductZone
    extra = 1
    tab = True
    hide_title = True


class CustomPlantAdmin(PlantAdmin):
    inlines = PlantAdmin.inlines + [TagInline] + [ProductZoneInline]


admin.site.unregister(Plant)
admin.site.register(Plant, CustomPlantAdmin)


class CustomPlanterAdmin(PlanterAdmin):
    inlines = PlanterAdmin.inlines + [TagInline] + [ProductZoneInline]


admin.site.unregister(Planter)
admin.site.register(Planter, CustomPlanterAdmin)


class CustomPlantingAccessoriesAdmin(PlantingAccessoriesAdmin):
    inlines = PlantingAccessoriesAdmin.inlines + [TagInline] + [ProductZoneInline]


admin.site.unregister(PlantingAccessories)
admin.site.register(PlantingAccessories, CustomPlantingAccessoriesAdmin)


class CustomServiceAdmin(ServiceAdmin):
    inlines = ServiceAdmin.inlines + [TagInline]


admin.site.unregister(Service)
admin.site.register(Service, CustomServiceAdmin)
