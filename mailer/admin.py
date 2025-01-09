from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Email
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Email)
class EmailAdmin(SummernoteModelAdmin, ModelAdmin):
    list_display = ('subject', 'sender', 'recipients', 'timestamp', 'is_draft')
    list_filter = ('sender', 'timestamp', 'is_draft')
    search_fields = ('subject', 'body', 'recipients')
    date_hierarchy = 'timestamp'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(sender=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj.sender == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj.sender == request.user

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If creating new email
            obj.sender = request.user
        super().save_model(request, obj, form, change)
