from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from unfold.admin import ModelAdmin

from .models import Category, Post


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}

    autocomplete_fields = ["categories"]

    search_fields = ["title", "content"]

    list_filter = ["author", "categories"]


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name", "post_count")
    prepopulated_fields = {"slug": ("name",)}

    search_fields = ["name"]

    @admin.display(ordering="post_count")
    def post_count(self, category):
        url = (
            reverse("admin:blog_post_changelist")
            + "?"
            + urlencode({"categories__id": str(category.id)})
        )
        return format_html(f"<a href='{url}'>{category.post_count}</a>")

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(post_count=Count("posts", distinct=True))
        )
