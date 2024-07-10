from django.contrib import admin
from .models import BannerImage, ContactInfo, AboutUs, OurClients, LegalDocument


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "alt_text", "created_at", "updated_at")
    search_fields = ("alt_text",)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "address", "created_at", "updated_at")
    search_fields = ("email", "phone", "address")


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("title",)


@admin.register(OurClients)
class OurClientsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo", "url", "created_at", "updated_at")
    search_fields = ("name", "url")


@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "document", "body", "created_at", "updated_at")
    search_fields = ("title",)
