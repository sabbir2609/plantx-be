import json
import os
from django.core.management.base import BaseCommand
from main.models import Planter


class Command(BaseCommand):
    help = "Generate fake planter data from a JSON file"

    def handle(self, *args, **kwargs):
        # Path to the JSON file
        file_path = os.path.join(os.path.dirname(__file__), "planters_data.json")

        # Load data from the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)

        # Create Planter objects
        for item in data:
            planter, created = Planter.objects.get_or_create(
                model=item["model"],
                defaults={
                    "planter_type": item["planter_type"],
                    "size": item["size"],
                    "color": item.get("color", ""),
                    "description": item.get("description", ""),
                    "inventory": item.get("inventory", 0),
                    "price": item.get("price", 0.0),
                },
            )

        self.stdout.write(self.style.SUCCESS("Successfully generated planter data"))
