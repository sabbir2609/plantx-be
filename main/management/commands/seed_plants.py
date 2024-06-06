import json
import os
from django.core.management.base import BaseCommand
from main.models import Plant, PlantCategory
from datetime import datetime


class Command(BaseCommand):
    help = "Generate fake plant data from a JSON file"

    def handle(self, *args, **kwargs):
        # Path to the JSON file
        file_path = os.path.join(os.path.dirname(__file__), "plants_data.json")

        # Load data from the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Create Plant objects
        for item in data:
            # Extract category ID from the data
            category_id = item.pop("category")

            # Fetch the corresponding PlantCategory instance
            category = PlantCategory.objects.get(id=category_id)

            # Create Plant object
            plant = Plant(
                title=item["title"],
                category=category,
                indoor_or_outdoor=item["indoor_or_outdoor"],
                size=item["size"],
                description=item.get("description", ""),
                care_instructions=item.get("care_instructions", ""),
                created_at=datetime.strptime(item["created_at"], "%Y-%m-%dT%H:%M:%SZ"),
            )
            plant.save()

            # Add tags
            tags = item.get("tags", [])
            plant.tags.set(tags)

        self.stdout.write(self.style.SUCCESS("Successfully generated plant data"))
