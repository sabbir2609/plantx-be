from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerImage(models.Model):

    class ScreenSizeChoices(models.TextChoices):
        SMALL_SCREEN = "Small Screen", _("Small Screen")
        LARGE_SCREEN = "Large Screen", _("Large Screen")

    image = models.ImageField(upload_to="banners/")
    screen_size = models.CharField(
        max_length=20,
        choices=ScreenSizeChoices.choices,
        help_text=_("Select the size of the plant."),
    )
    alt_text = models.CharField(
        max_length=255,
        help_text="Please provide a short description of the image.",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"


class ContactInfo(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"


class OurClients(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="clients/")
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Our Client"
        verbose_name_plural = "Our Clients"


class LegalDocument(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(
        upload_to="legal/",
        null=True,
        blank=True,
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Legal Document"
        verbose_name_plural = "Legal Documents"
