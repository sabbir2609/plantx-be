from django.core.management.base import BaseCommand
from main.models import Promotion


class Command(BaseCommand):
    help = "Populate the database with 10 promotions"

    def handle(self, *args, **kwargs):
        promotions = [
            {"description": "Summer Sale - Up to 20% off!", "discount": 20.0},
            {"description": "Buy One Get One Free", "discount": None},
            {"description": "Free Shipping on orders over $50", "discount": None},
            {"description": "20% off all succulents", "discount": 20.0},
            {"description": "Holiday Special - 15% off", "discount": 15.0},
            {"description": "Clearance Sale - 50% off select items", "discount": 50.0},
            {"description": "Spring Sale - 10% off all orders", "discount": 10.0},
            {"description": "New Arrivals - 5% off", "discount": 5.0},
            {"description": "End of Season Sale - Up to 30% off", "discount": 30.0},
            {"description": "Flash Sale - 25% off for 24 hours", "discount": 25.0},
        ]

        for promo_data in promotions:
            promo, created = Promotion.objects.get_or_create(
                description=promo_data["description"],
                defaults={"discount": promo_data["discount"]},
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully created promotion: {promo.description}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Promotion already exists: {promo.description}")
                )
