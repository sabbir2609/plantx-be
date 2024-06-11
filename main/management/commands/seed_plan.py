from django.core.management.base import BaseCommand
from main.models import ServiceType, ServiceTypeFeature


class Command(BaseCommand):
    help = "Seeds the database with plans"

    def handle(self, *args, **options):
        plans = [
            {
                "id": 1,
                "title": "Starter",
                "description": "Ideal for introducing a touch of nature to your home with basic design services.",
                "features": [
                    "Basic Consultation",
                    "Plant Selection Guide",
                    "DIY Plant Care Kit",
                ],
                "price": "$50/month",
            },
            {
                "id": 2,
                "title": "Business",
                "description": "Enhance your office environment with our curated plant decor solutions.",
                "features": [
                    "On-site Consultation",
                    "Plant Installation",
                    "Monthly Maintenance",
                ],
                "price": "$150/month",
            },
            {
                "id": 3,
                "title": "Premium",
                "description": "Comprehensive plant decor solutions to transform your space into a green haven.",
                "features": [
                    "Custom Design Plan",
                    "Premium Plant Selection",
                    "Bi-Weekly Maintenance",
                ],
                "price": "$300/month",
            },
            {
                "id": 4,
                "title": "Enterprise",
                "description": "Bespoke plant decor solutions for large-scale projects with dedicated support.",
                "features": [
                    "Dedicated Project Manager",
                    "Custom Design and Installation",
                    "Regular Maintenance and Support",
                ],
                "price": "Contact Us",
            },
        ]

        for plan in plans:
            # Create the ServiceType instance
            service_type = ServiceType.objects.create(
                id=plan["id"], title=plan["title"], description=plan["description"]
            )

            # Create the ServiceTypeFeature instances associated with the ServiceType
            for feature in plan["features"]:
                ServiceTypeFeature.objects.create(
                    title=feature, service_type=service_type
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded database with plans"))
