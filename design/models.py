from django.db import models
from django.utils.translation import gettext_lazy as _


class DesignCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(
        blank=True, null=True, help_text=_("A short description of the category")
    )
    image = models.ImageField(
        upload_to="design_categories/",
        help_text=_("An image representing the category"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Design Category")
        verbose_name_plural = _("Design Categories")

    def __str__(self):
        return self.name


class Design(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(
        DesignCategory, on_delete=models.CASCADE, related_name="designs"
    )
    description = models.TextField(
        blank=True, null=True, help_text=_("A short description of the design")
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Design")
        verbose_name_plural = _("Designs")

    def __str__(self):
        return self.name


class DesignImage(models.Model):
    design = models.ForeignKey(
        Design,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="designs/")
    alt_text = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Design Image")
        verbose_name_plural = _("Design Images")

    def __str__(self):
        return self.design.name
