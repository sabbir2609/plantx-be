from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, help_text=_("Enter the category name"))
    slug = models.SlugField(
        unique=True, help_text=_("Enter a unique slug for the category")
    )
    short_description = models.CharField(
        max_length=255,
        help_text=_("Enter a short description of the category"),
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="blog/categories/",
        blank=True,
        null=True,
        help_text=_("Upload an image for the category"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Categories")
        ordering = ["name"]


class Post(models.Model):
    title = models.CharField(max_length=255, help_text=_("Enter the post title"))
    slug = models.SlugField(
        unique=True, help_text=_("Enter a unique slug for the post")
    )
    content = models.TextField(help_text=_("Enter the content of the post"))
    image = models.ImageField(
        upload_to="blog/posts/",
        blank=True,
        null=True,
        help_text=_("Upload an image for the post"),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        help_text=_("Select the author of the post"),
    )
    categories = models.ManyToManyField(
        Category, related_name="posts", help_text=_("Select categories for the post")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text=_("The date and time the post was created")
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text=_("The date and time the post was last updated")
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = _("Posts")
