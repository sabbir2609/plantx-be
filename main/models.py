from django.db import models
from taggit.managers import TaggableManager


class Plant(models.Model):
    class PlantType(models.TextChoices):
        INDOOR = "indoor", "Indoor"
        OUTDOOR = "outdoor", "Outdoor"
        BOTH = "both", "Both"

    class PlantCategory(models.TextChoices):
        FLOWERING = "flowering", "Flowering"
        NON_FLOWERING = "non-flowering", "Non-flowering"
        SUCCULENT = "succulent", "Succulent"
        TROPICAL = "tropical", "Tropical"
        HERB = "herb", "Herb"
        FRUIT = "fruit", "Fruit"

    name = models.CharField(max_length=255, unique=True)
    plant_type = models.CharField(
        max_length=10, choices=PlantType.choices, default=PlantType.INDOOR, blank=True
    )
    category = models.CharField(
        max_length=20,
        choices=PlantCategory.choices,
        default=PlantCategory.FLOWERING,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)
    care_instructions = models.TextField(null=True, blank=True)
    is_pet_friendly = models.BooleanField(default=True)
    benefits = models.TextField(null=True, blank=True)
    tags = TaggableManager()

    inventory = models.PositiveIntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Plant"
        verbose_name_plural = "Plants"


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="plants/")

    def __str__(self):
        return f"{self.plant.name} Image"

    class Meta:
        verbose_name = "Plant Image"
        verbose_name_plural = "Plant Images"


class Planter(models.Model):
    class PlanterType(models.TextChoices):
        CERAMIC = "ceramic", "Ceramic"
        PLASTIC = "plastic", "Plastic"
        METAL = "metal", "Metal"
        WOOD = "wood", "Wood"
        STONE = "stone", "Stone"
        Terracotta = "terracotta", "Terracotta"

    class PlanterSize(models.TextChoices):
        SMALL = "small", "Small"
        MEDIUM = "medium", "Medium"
        LARGE = "large", "Large"
        XLARGE = "xlarge", "X-Large"

    model = models.CharField(max_length=255, unique=True)
    planter_type = models.CharField(
        max_length=20, choices=PlanterType.choices, default=PlanterType.CERAMIC
    )
    size = models.CharField(
        max_length=10, choices=PlanterSize.choices, default=PlanterSize.MEDIUM
    )
    color = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    inventory = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Planter"
        verbose_name_plural = "Planters"


class PlanterImage(models.Model):
    planter = models.ForeignKey(
        Planter, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="planters/")

    def __str__(self):
        return f"{self.planter.model} Image"

    class Meta:
        verbose_name = "Planter Image"
        verbose_name_plural = "Planter Images"


class InteriorDesignService(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Interior Design Service"
        verbose_name_plural = "Interior Design Services"


class InteriorDesignServiceImage(models.Model):
    service = models.ForeignKey(
        InteriorDesignService, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return f"{self.service.name} Image"

    class Meta:
        verbose_name = "Interior Design Service Image"
        verbose_name_plural = "Interior Design Service Images"
