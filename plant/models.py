from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PlantCategory(models.Model):
    name = models.CharField(
        max_length=255, unique=True, help_text=_("The name of the category.")
    )
    slug = models.SlugField(
        max_length=255, unique=True, help_text=_("A unique slug for the category.")
    )
    description = models.TextField(
        null=True, blank=True, help_text=_("A brief description of the category.")
    )
    image = models.ImageField(
        upload_to="plant_category/",
        help_text=_("An image representing the category."),
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Plant(models.Model):
    name = models.CharField(
        max_length=255, unique=True, help_text=_("The common name of the plant.")
    )
    slug = models.SlugField(
        max_length=255, unique=True, help_text=_("A unique slug for the plant.")
    )
    category = models.ForeignKey(
        PlantCategory,
        on_delete=models.CASCADE,
        help_text=_("The category to which the plant belongs."),
        related_name="plant_category",
    )
    scientific_name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=_("The scientific name of the plant."),
    )

    toxicity = models.CharField(
        max_length=255,
        help_text=_("Information about the plant's toxicity to pets and humans."),
    )

    is_pet_safe = models.BooleanField(
        default=True,
        help_text=_("Whether the plant is safe for pets."),
    )

    is_air_purifying = models.BooleanField(
        default=False,
        help_text=_("Whether the plant is an air purifier."),
    )

    description = models.TextField(
        null=True, blank=True, help_text=_("A brief description of the plant.")
    )
    care_instructions = models.TextField(
        null=True, blank=True, help_text=_("Instructions on how to care for the plant.")
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("The price of the plant."),
    )

    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Plant")
        verbose_name_plural = _("Plants")
        unique_together = ["name", "scientific_name"]

    def __str__(self):
        return self.name


class PlantImage(models.Model):
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        help_text=_("The plant the image belongs to."),
    )
    image = models.ImageField(upload_to="plant/", help_text=_("An image of the plant."))
    alt_text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("A brief description of the image."),
    )
    source = models.CharField(
        max_length=255, null=True, blank=True, help_text=_("The source of the image.")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Plant Image")
        verbose_name_plural = _("Plant Images")

    def __str__(self):
        return self.plant.name


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("The user who wrote the review.")
    )
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, help_text=_("The plant being reviewed.")
    )
    rating = models.IntegerField(help_text=_("The rating given to the plant (1-5)."))
    comment = models.TextField(help_text=_("The content of the review."))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"{self.user.username} - {self.plant.name}"


class ReviewImage(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        help_text=_("The review the image belongs to."),
    )
    image = models.ImageField(help_text=_("An image related to the review."))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Review Image")
        verbose_name_plural = _("Review Images")

    def __str__(self):
        return self.review.plant.name
