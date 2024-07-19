from django.contrib import admin
from .models import BannerImage, ContactInfo, OurClients, LegalDocument
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
