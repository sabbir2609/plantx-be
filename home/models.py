from django.db import models


class BannerImage(models.Model):
    class ScreenSizeChoices(models.TextChoices):
        SMALL_SCREEN = "Small Screen", ("Small Screen")
        LARGE_SCREEN = "Large Screen", ("Large Screen")

    image = models.ImageField(upload_to="banners/")
    screen_size = models.CharField(
        max_length=20,
        choices=ScreenSizeChoices.choices,
    )
    alt_text = models.CharField(
        default="Banner Image",
        max_length=255,
    )

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Banner Image"
        verbose_name_plural = "Banner Images"


class ContactInfo(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    facebook = models.URLField(null=True, blank=True)
    x = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    pinterest = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"


class OurClients(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="clients/")
    url = models.URLField()

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Legal Document"
        verbose_name_plural = "Legal Documents"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
