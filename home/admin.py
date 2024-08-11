from django.contrib import admin
from .models import BannerImage, ContactInfo, OurClients, LegalDocument, ContactMessage
from unfold.admin import ModelAdmin


@admin.register(BannerImage)
class BannerImageAdmin(ModelAdmin):
    list_display = ("id", "alt_text", "screen_size")
    search_fields = ("alt_text",)
    list_filter = ("screen_size",)


@admin.register(ContactInfo)
class ContactInfoAdmin(ModelAdmin):
    list_display = ("email", "phone", "address")
    search_fields = ("email", "phone", "address")

    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(OurClients)
class OurClientsAdmin(ModelAdmin):
    list_display = ("name", "logo", "url", "id")
    search_fields = ("name", "url")


@admin.register(LegalDocument)
class LegalDocumentAdmin(ModelAdmin):
    list_display = ("title", "document", "body")
    search_fields = ("title",)


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ("name", "email", "sent_at", "is_read")
    search_fields = ("name", "email", "message")
    list_filter = ("sent_at",)
    date_hierarchy = "sent_at"
    actions = ["mark_as_read"]
    list_per_page = 10

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected messages marked as read.")

    mark_as_read.short_description = "Mark selected messages as read"
