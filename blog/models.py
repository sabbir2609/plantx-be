from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=255, unique=True, help_text=_("The name of the category.")
    )
    description = models.TextField(help_text=_("A brief description of the category."))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, help_text=_("The title of the blog post."))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text=_("The category of the blog post."),
    )
    content = models.TextField(help_text=_("The content of the blog post."))
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("The author of the blog post.")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")

    def __str__(self):
        return self.title
