from django.contrib import admin
from .models import Tag
from unfold.admin import ModelAdmin


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    search_fields = ["label"]
