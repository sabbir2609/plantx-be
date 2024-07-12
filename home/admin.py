from django.contrib import admin
from .models import BannerImage, ContactInfo, OurClients, LegalDocument

from django.utils.html import format_html


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("alt_text", "image", "id")
    search_fields = ("alt_text",)
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" class="thumbnail" style="max-width: 200px;"/>'
            )
        return ""


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "address")
    search_fields = ("email", "phone", "address")

    def has_add_permission(self, request):
        if ContactInfo.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(OurClients)
class OurClientsAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "url", "id")
    search_fields = ("name", "url")
    readonly_fields = ("thumbnail",)

    def thumbnail(self, instance):
        if instance.logo.name != "":
            return format_html(
                f'<img src="{instance.logo.url}" class="thumbnail" style="max-width: 200px;"/>'
            )
        return ""


@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "document", "body")
    search_fields = ("title",)
