import json
import os
from django.core.management.base import BaseCommand
from main.models import Plant
from taggit.models import Tag


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
            plant = Plant.objects.create(
                name=item["name"],
                plant_type=item["plant_type"],
                category=item["category"],
                description=item.get("description", ""),
                care_instructions=item.get("care_instructions", ""),
                is_pet_friendly=item.get("is_pet_friendly", True),
                benefits=item.get("benefits", ""),
                inventory=item.get("inventory", 0),
                price=item.get("price", 0.0),
            )

            # Add tags
            for tag_name in item["tags"]:
                plant.tags.add(tag_name)

            plant.save()

        self.stdout.write(self.style.SUCCESS("Successfully generated plant data"))
