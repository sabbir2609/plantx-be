import os
import random
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from tags.models import TaggedItem
from zone.models import ProductZone

from . import validators


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="customers/",
        null=True,
        blank=True,
        validators=[validators.validate_file_size],
    )
    phone = models.CharField(max_length=255)
    address = models.TextField(
        blank=True, null=True, help_text="Address of the customer"
    )
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ["user__last_name", "user__first_name"]
        permissions = [("view_history", "Can View History")]

    @admin.display(ordering="user__first_name")
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering="user__last_name")
    def last_name(self):
        return self.user.last_name


def upload_to(instance, filename):
    model_name = slugify(instance.content_type.model)
    instance_slug = slugify(
        getattr(instance.content_object, "slug", instance.object_id)
    )
    return os.path.join("images", model_name, instance_slug, filename)


class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    image = models.ImageField(
        upload_to=upload_to, validators=[validators.validate_file_size]
    )
    short_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return f"{self.content_type.name}: {self.content_object} - {self.image}"


class Feature(models.Model):
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Discount in percentage, if any",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return self.description


class BaseProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(
        max_length=20, blank=True, null=True, unique=True, editable=False
    )
    inventory = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Number of items in stock",
    )

    images = GenericRelation(Image, related_name="images")
    features = GenericRelation(Feature, related_name="features")
    zones = GenericRelation(ProductZone, related_name="zones")
    tags = GenericRelation(TaggedItem, related_name="tags")

    promotion = models.ManyToManyField("Promotion", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def generate_sku(self):
        raise NotImplementedError("Subclasses must implement generate_sku method")

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PlantCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="plant_categories/",
        null=True,
        blank=True,
        validators=[validators.validate_file_size],
    )

    featured_plant = models.ForeignKey(
        "Plant", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Plant Category"
        verbose_name_plural = "Plant Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Plant(BaseProduct):
    class LocationChoices(models.TextChoices):
        INDOOR = "Indoor", "Indoor"
        OUTDOOR = "Outdoor", "Outdoor"
        BOTH = "Both", "Both"

    class SizeChoices(models.TextChoices):
        SMALL = "Small", "Small"
        MEDIUM = "Medium", "Medium"
        LARGE = "Large", "Large"
        EXTRA_LARGE = "Extra Large", "Extra Large"

    size = models.CharField(max_length=20, blank=True, choices=SizeChoices.choices)
    category = models.ForeignKey("PlantCategory", on_delete=models.PROTECT)
    location_type = models.CharField(
        default=LocationChoices.BOTH,
        null=True,
        blank=True,
        max_length=20,
        choices=LocationChoices.choices,
    )
    care_instructions = models.TextField(blank=True, null=True)

    images = GenericRelation(Image)
    features = GenericRelation(Feature)
    tags = GenericRelation(TaggedItem)
    zones = GenericRelation(ProductZone)

    def generate_sku(self):
        return f"PL{self.name[:2].upper()}{self.category.name[:3].upper()}{random.randint(100, 999)}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Plant"
        verbose_name_plural = "Plants"


class PlanterCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="planter_categories/", blank=True, null=True)

    featured_planter = models.ForeignKey(
        "Planter", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Planter Category"
        verbose_name_plural = "Planter Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Planter(BaseProduct):
    category = models.ForeignKey(PlanterCategory, on_delete=models.CASCADE)
    size = models.CharField(
        max_length=20, blank=True, null=True, help_text="Size in inches"
    )
    color = models.CharField(max_length=50, blank=True, null=True)
    is_custom = models.BooleanField(default=False)

    def generate_sku(self):
        return f"PT{self.name[:2].upper()}{self.category.name[:3].upper()}{random.randint(100, 999)}"

    class Meta:
        verbose_name = "Planter"
        verbose_name_plural = "Planters"
        ordering = ["-updated_at"]


class PlantingAccessoriesCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="planting_accessories_categories/", blank=True, null=True
    )

    class Meta:
        verbose_name = "Planting Accessory Category"
        verbose_name_plural = "Planting Accessory Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlantingAccessories(BaseProduct):
    category = models.ForeignKey(PlantingAccessoriesCategory, on_delete=models.CASCADE)

    def generate_sku(self):
        return f"PA{self.name[:2].upper()}{self.category.name[:3].upper()}{random.randint(100, 999)}"

    class Meta:
        verbose_name = "Planting Accessory"
        verbose_name_plural = "Planting Accessories"
        ordering = ["name"]


class ServiceCategory(models.Model):
    class TypeChoices(models.TextChoices):
        COMMERCIAL = "Commercial", "Commercial"
        RESIDENTIAL = "Residential", "Residential"

    serial = models.PositiveSmallIntegerField(unique=True)
    type = models.CharField(
        default=TypeChoices.RESIDENTIAL,
        null=True,
        blank=True,
        max_length=20,
        choices=TypeChoices.choices,
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="service_categories/",
        null=True,
        blank=True,
        validators=[validators.validate_file_size],
    )

    class Meta:
        unique_together = ["title", "type"]
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        ordering = ["serial"]

    def __str__(self):
        return f"{self.type}-{self.title}"


class Service(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(ServiceCategory, blank=True)

    def get_categories(self):
        return ", ".join(
            [
                f"{category.title} ({category.type})"
                for category in self.categories.all()
            ]
        )

    get_categories.short_description = "Categories"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Ideas(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to="ideas/",
        null=True,
        blank=True,
        validators=[validators.validate_file_size],
    )
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Idea"
        verbose_name_plural = "Ideas"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_slug(self):
        return (
            f"{self.customer.user.first_name}-{self.customer.user.last_name}".replace(
                " ", "-"
            )
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ["-created_at"]

    def __str__(self):
        return self.customer.user.full_name


class Team(models.Model):
    serial = models.PositiveSmallIntegerField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    position = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="team_members/",
        null=True,
        blank=True,
        validators=[validators.validate_file_size],
    )
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_slug(self):
        return f"{self.user.first_name}-{self.user.last_name}".replace(" ", "-")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"
        ordering = ["serial"]

    def __str__(self):
        return self.user.full_name


class TeamContact(models.Model):
    team = models.ForeignKey(Team, related_name="contacts", on_delete=models.CASCADE)
    social_media_name = models.CharField(max_length=255)
    social_media_link = models.URLField()

    class Meta:
        verbose_name = "Team Contact"
        verbose_name_plural = "Team Contacts"

    def __str__(self):
        return f"{self.team.user.full_name} - {self.social_media_name}"


class Projects(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    categories = models.ManyToManyField(ServiceCategory, blank=True)
    description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-year"]

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to="events/",
        null=True,
        blank=True,
        validators=[validators.validate_file_size],
    )
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_upcoming = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-start_date"]

    def __str__(self):
        return self.title
