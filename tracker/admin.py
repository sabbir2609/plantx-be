from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TrackLinks


@admin.register(TrackLinks)
class TrackLinksAdmin(ModelAdmin):
    list_display = (
        "link_display",
        "id",
        "visit_time",
        "ip_address",
        "referrer",
    )
    search_fields = ("link", "referrer", "user_agent", "ip_address")
    list_filter = ("visit_time", "user_agent")
    date_hierarchy = "visit_time"
    list_per_page = 25
    ordering = ("-visit_time",)

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": ("link", "visit_time"),
                "classes": ("wide",),
            },
        ),
        (
            "Visitor Details",
            {
                "fields": ("ip_address", "user_agent", "referrer"),
                "classes": ("collapse",),
                "description": "Technical information about the visitor",
            },
        ),
    )

    readonly_fields = ("link", "visit_time", "referrer", "user_agent", "ip_address")
    save_on_top = True
    actions_on_top = True
    actions_on_bottom = False

    def link_display(self, obj):
        # display only the domain name, no fromatting
        return obj.link.split("/")[2]
