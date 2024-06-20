# main/management/commands/seed_planters.py

from django.core.management.base import BaseCommand
from main.models import PlanterCategory, Planter


class Command(BaseCommand):
    help = "Populate the database with planter categories and sample planters"

    def handle(self, *args, **kwargs):
        planter_categories = [
            {
                "name": "Indoor Planters",
                "description": "Planters suitable for indoor environments.",
            },
            {
                "name": "Outdoor Planters",
                "description": "Planters suitable for outdoor environments.",
            },
            {
                "name": "Hanging Planters",
                "description": "Planters that can be hung from ceilings or walls.",
            },
            {
                "name": "Self-Watering Planters",
                "description": "Planters with self-watering features.",
            },
            {
                "name": "Decorative Planters",
                "description": "Planters with decorative designs.",
            },
        ]

        sample_planters = [
            {
                "model": "Classic Indoor Planter",
                "size": "Medium",
                "description": "A classic planter for indoor plants.",
                "color": "White",
                "category": "Indoor Planters",
                "is_custom": False,
            },
            {
                "model": "Outdoor Garden Planter",
                "size": "Large",
                "description": "A large planter for outdoor gardens.",
                "color": "Terracotta",
                "category": "Outdoor Planters",
                "is_custom": False,
            },
            {
                "model": "Modern Hanging Planter",
                "size": "Small",
                "description": "A stylish hanging planter for modern homes.",
                "color": "Black",
                "category": "Hanging Planters",
                "is_custom": False,
            },
            {
                "model": "Self-Watering Herb Planter",
                "size": "Small",
                "description": "A self-watering planter perfect for herbs.",
                "color": "Green",
                "category": "Self-Watering Planters",
                "is_custom": True,
            },
            {
                "model": "Decorative Ceramic Planter",
                "size": "Medium",
                "description": "A decorative ceramic planter.",
                "color": "Blue",
                "category": "Decorative Planters",
                "is_custom": False,
            },
            {
                "model": "Custom Indoor Planter",
                "size": "Large",
                "description": "A custom indoor planter with a unique design.",
                "color": "Custom",
                "category": "Indoor Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Outdoor Planter",
                "size": "Medium",
                "description": "A custom outdoor planter with a unique design.",
                "color": "Custom",
                "category": "Outdoor Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Hanging Planter",
                "size": "Small",
                "description": "A custom hanging planter with a unique design.",
                "color": "Custom",
                "category": "Hanging Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Self-Watering Planter",
                "size": "Medium",
                "description": "A custom self-watering planter with a unique design.",
                "color": "Custom",
                "category": "Self-Watering Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Decorative Planter",
                "size": "Large",
                "description": "A custom decorative planter with a unique design.",
                "color": "Custom",
                "category": "Decorative Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Planter",
                "size": "Medium",
                "description": "A custom planter with a unique design.",
                "color": "Custom",
                "category": "Indoor Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Planter",
                "size": "Large",
                "description": "A custom planter with a unique design.",
                "color": "Custom",
                "category": "Outdoor Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Planter",
                "size": "Small",
                "description": "A custom planter with a unique design.",
                "color": "Custom",
                "category": "Hanging Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Planter",
                "size": "Medium",
                "description": "A custom planter with a unique design.",
                "color": "Custom",
                "category": "Self-Watering Planters",
                "is_custom": True,
            },
            {
                "model": "Custom Planter",
                "size": "Large",
                "description": "A custom planter with a unique design.",
                "color": "Custom",
                "category": "Decorative Planters",
                "is_custom": True,
            },
        ]

        # Create planter categories
        for category in planter_categories:
            PlanterCategory.objects.get_or_create(
                name=category["name"], defaults={"description": category["description"]}
            )

        # Create sample planters
        for planter in sample_planters:
            category = PlanterCategory.objects.get(name=planter["category"])
            Planter.objects.get_or_create(
                model=planter["model"],
                defaults={
                    "size": planter["size"],
                    "description": planter["description"],
                    "color": planter["color"],
                    "category": category,
                    "is_custom": planter["is_custom"],
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully populated the database with planter categories and sample planters"
            )
        )
