from django.core.management.base import BaseCommand
from main.models import PlantFeatures


class Command(BaseCommand):
    help = "Populate the database with 10 plant feature names"

    def handle(self, *args, **kwargs):
        features = [
            "Thornless",
            "Variegated leaves",
            "Fragrant flowers",
            "Drought-tolerant",
            "Evergreen",
            "Edible",
            "Attractive bark",
            "Medicinal properties",
            "Attracts pollinators",
            "Low maintenance",
        ]

        for feature_name in features:
            feature, created = PlantFeatures.objects.get_or_create(name=feature_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created feature: {feature.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Feature already exists: {feature.name}")
                )
