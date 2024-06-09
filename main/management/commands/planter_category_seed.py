from django.core.management.base import BaseCommand
from main.models import PlanterCategory


class Command(BaseCommand):
    help = "Seed the database with initial PlanterCategory data"

    def handle(self, *args, **kwargs):
        categories = [
            "Plastic",
            "Wooden",
            "Metal",
            "Glass",
            "Concrete",
            "Terracotta",
            "Foam",
            "Glazed Ceramic",
            "Fiberglass",
            "Resin",
        ]

        for category_name in categories:
            PlanterCategory.objects.get_or_create(name=category_name)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully seeded the database with planter categories"
            )
        )
