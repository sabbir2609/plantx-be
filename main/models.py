from django.db import models


class PlantCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="plant_categories/", null=True, blank=True)

    class Meta:
        verbose_name = "Plant Category"
        verbose_name_plural = "Plant Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlantFeatures(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Plant Feature"
        verbose_name_plural = "Plant Features"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Plant(models.Model):
    class IndoorOutdoorChoices(models.TextChoices):
        INDOOR = "Indoor", "Indoor"
        OUTDOOR = "Outdoor", "Outdoor"

    class SizeChoices(models.TextChoices):
        SMALL = "Small", "Small"
        MEDIUM = "Medium", "Medium"
        LARGE = "Large", "Large"
        EXTRA_LARGE = "Extra Large", "Extra Large"

    title = models.CharField(max_length=100)
    category = models.ForeignKey(PlantCategory, on_delete=models.CASCADE)
    indoor_or_outdoor = models.CharField(
        max_length=10, choices=IndoorOutdoorChoices.choices)
    size = models.CharField(max_length=20, choices=SizeChoices.choices)
    description = models.TextField(blank=True, null=True)
    care_instructions = models.TextField(blank=True, null=True)
    features = models.ManyToManyField(PlantFeatures, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.title


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="plant_images/")
    short_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Plant Image"
        verbose_name_plural = "Plant Images"


class PlanterCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="planter_categories/", blank=True, null=True)

    class Meta:
        verbose_name = "Planter Category"
        verbose_name_plural = "Planter Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class PlanterFeatures(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Planter Feature"
        verbose_name_plural = "Planter Features"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Planter(models.Model):
    model = models.CharField(max_length=100)
    category = models.ForeignKey(PlanterCategory, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    features = models.ManyToManyField(PlanterFeatures, blank=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    is_custom = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Planter"
        verbose_name_plural = "Planters"
        ordering = ["model"]

    def __str__(self):
        return self.model


class PlanterImage(models.Model):
    planter = models.ForeignKey(Planter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="planter_images/")
    short_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Planter Image"
        verbose_name_plural = "Planter Images"


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
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="service_categories/", null=True, blank=True)

    class Meta:
        unique_together = ["title", "type"]
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        ordering = ["serial"]

    def __str__(self):
        return f"{self.type}-{self.title}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(ServiceCategory, blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["title"]

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="service_images/")
    short_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.short_description

    class Meta:
        verbose_name = "Service Image"
        verbose_name_plural = "Service Images"


class Ideas(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="ideas/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Idea"
        verbose_name_plural = "Ideas"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Team(models.Model):
    serial = models.PositiveSmallIntegerField(unique=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team_members/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ["serial"]

    def __str__(self):
        return self.name


class TeamContact(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    social_media_name = models.CharField(max_length=100)
    social_media_link = models.URLField()

    class Meta:
        verbose_name = "Team Contact"
        verbose_name_plural = "Team Contacts"

    def __str__(self):
        return self.team.name


class Projects(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(ServiceCategory, blank=True)
    description = models.TextField(null=True, blank=True)
    client = models.CharField(max_length=100, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["title"]

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images/")
    short_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"
