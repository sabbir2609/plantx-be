import random
from django.core.management.base import BaseCommand
from main.models import Planter, PlanterCategory


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        planters_data = [
            {
                "model": "Model 91",
                "size": "Extra Large",
                "description": "Unique and decorative",
                "color": "Purple",
            },
            {
                "model": "Model 17",
                "size": "Medium",
                "description": "Breathable material for healthy roots",
                "color": "Brown",
            },
            {
                "model": "Model 19",
                "size": "Small",
                "description": "Elegant and modern design",
                "color": "White",
            },
            {
                "model": "Model 64",
                "size": "Extra Large",
                "description": "Portable and convenient",
                "color": "Black",
            },
            {
                "model": "Model 81",
                "size": "Extra Large",
                "description": "Comes with drainage holes",
                "color": "Blue",
            },
            {
                "model": "Model 45",
                "size": "Medium",
                "description": "Weather-resistant and sturdy",
                "color": "White",
            },
            {
                "model": "Model 38",
                "size": "Extra Large",
                "description": "Handcrafted with care",
                "color": "Orange",
            },
            {
                "model": "Model 47",
                "size": "Extra Large",
                "description": "Space-saving design",
                "color": "Purple",
            },
            {
                "model": "Model 41",
                "size": "Small",
                "description": "High-quality and long-lasting",
                "color": "Red",
            },
            {
                "model": "Model 80",
                "size": "Medium",
                "description": "Elegant and modern design",
                "color": "White",
            },
            {
                "model": "Model 5",
                "size": "Large",
                "description": "UV-resistant finish",
                "color": "Black",
            },
            {
                "model": "Model 54",
                "size": "Small",
                "description": "Minimalistic design",
                "color": "Black",
            },
            {
                "model": "Model 79",
                "size": "Medium",
                "description": "Textured surface for added appeal",
                "color": "Yellow",
            },
            {
                "model": "Model 38",
                "size": "Small",
                "description": "Space-saving design",
                "color": "Purple",
            },
            {
                "model": "Model 74",
                "size": "Small",
                "description": "UV-resistant finish",
                "color": "Yellow",
            },
            {
                "model": "Model 77",
                "size": "Small",
                "description": "Versatile for indoor and outdoor use",
                "color": "White",
            },
            {
                "model": "Model 17",
                "size": "Large",
                "description": "Minimalistic design",
                "color": "Pink",
            },
            {
                "model": "Model 61",
                "size": "Extra Large",
                "description": "Lightweight and durable",
                "color": "Grey",
            },
            {
                "model": "Model 99",
                "size": "Large",
                "description": "Minimalistic design",
                "color": "Pink",
            },
            {
                "model": "Model 59",
                "size": "Large",
                "description": "Handcrafted with care",
                "color": "Grey",
            },
        ]

        categories = list(PlanterCategory.objects.all())
        if not categories:
            self.stdout.write(
                self.style.ERROR("No PlanterCategory instances found in the database.")
            )
            return

        for planter_data in planters_data:
            planter_data["category"] = random.choice(categories)
            Planter.objects.create(**planter_data)

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded the database with planters data")
        )
