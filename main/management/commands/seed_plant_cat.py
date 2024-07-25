from django.core.management.base import BaseCommand
from main.models import PlantCategory


class Command(BaseCommand):
    help = "Populate the database with 10 plant categories and their descriptions"

    def handle(self, *args, **kwargs):
        categories = [
            {
                "name": "Succulents",
                "description": "Drought-resistant plants with thick, fleshy parts.",
            },
            {
                "name": "Ferns",
                "description": "Plants with feathery leaves that thrive in humid environments.",
            },
            {
                "name": "Orchids",
                "description": "Exotic flowers known for their colorful and fragrant blooms.",
            },
            {
                "name": "Cacti",
                "description": "Spiny plants adapted to arid environments.",
            },
            {
                "name": "Herbs",
                "description": "Plants grown for their culinary and medicinal properties.",
            },
            {
                "name": "Bonsai",
                "description": "Miniature trees cultivated for aesthetic purposes.",
            },
            {
                "name": "Palms",
                "description": "Tropical plants with long, arching fronds.",
            },
            {
                "name": "Carnivorous Plants",
                "description": "Plants that derive nutrients by trapping and digesting insects.",
            },
            {
                "name": "Flowering Plants",
                "description": "Plants known for their vibrant and beautiful flowers.",
            },
            {
                "name": "Foliage Plants",
                "description": "Plants prized for their attractive and decorative leaves.",
            },
        ]

        for category_data in categories:
            category, created = PlantCategory.objects.get_or_create(
                name=category_data["name"],
                defaults={"description": category_data["description"]},
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully created category: {category.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Category already exists: {category.name}")
                )
