import json
import random
from django.core.management.base import BaseCommand
from main.models import Service, ServiceCategory, ServiceType


class Command(BaseCommand):
    help = "Populate the database with service data"

    def handle(self, *args, **kwargs):
        data = [
            {
                "id": 1,
                "title": "Starter Plan",
                "description": "Affordable plant decor solutions for small spaces. Ideal for beginners.",
                "budget_range": "$50 - $150",
            },
            {
                "id": 2,
                "title": "Business Plan",
                "description": "Professional plant decor for office spaces. Enhance your workspace environment.",
                "budget_range": "$300 - $700",
            },
            {
                "id": 3,
                "title": "Premium Plan",
                "description": "Luxury plant decor solutions for homes and offices. High-end designs and premium plants.",
                "budget_range": "$700 - $1500",
            },
            {
                "id": 4,
                "title": "Enterprise Plan",
                "description": "Comprehensive plant decor solutions for large commercial spaces. Customized designs.",
                "budget_range": "$1500 - $3000",
            },
            {
                "id": 5,
                "title": "Indoor Oasis",
                "description": "Create a lush indoor garden with our expert plant decor services.",
                "budget_range": "$200 - $600",
            },
            {
                "id": 6,
                "title": "Outdoor Retreat",
                "description": "Transform your outdoor space into a beautiful retreat with our plant decor services.",
                "budget_range": "$500 - $1200",
            },
            {
                "id": 7,
                "title": "Eco-Friendly Design",
                "description": "Sustainable plant decor solutions using eco-friendly materials and practices.",
                "budget_range": "$100 - $500",
            },
            {
                "id": 8,
                "title": "Modern Minimalist",
                "description": "Sleek and modern plant decor for contemporary spaces.",
                "budget_range": "$200 - $800",
            },
            {
                "id": 9,
                "title": "Zen Garden",
                "description": "Create a peaceful and relaxing atmosphere with our Zen garden decor services.",
                "budget_range": "$300 - $900",
            },
            {
                "id": 10,
                "title": "Tropical Paradise",
                "description": "Bring the tropics to your space with our tropical plant decor services.",
                "budget_range": "$400 - $1000",
            },
            {
                "id": 11,
                "title": "Succulent Collection",
                "description": "Stylish and low-maintenance succulent plant decor for any space.",
                "budget_range": "$50 - $300",
            },
            {
                "id": 12,
                "title": "Botanical Wall",
                "description": "Vertical garden solutions to create stunning botanical walls.",
                "budget_range": "$500 - $1500",
            },
            {
                "id": 13,
                "title": "Pet-Friendly Plants",
                "description": "Safe and beautiful plant decor options for homes with pets.",
                "budget_range": "$100 - $400",
            },
            {
                "id": 14,
                "title": "Seasonal Decor",
                "description": "Plant decor that changes with the seasons to keep your space fresh and vibrant.",
                "budget_range": "$200 - $700",
            },
            {
                "id": 15,
                "title": "Air-Purifying Plants",
                "description": "Improve indoor air quality with our selection of air-purifying plants.",
                "budget_range": "$150 - $500",
            },
            {
                "id": 16,
                "title": "Exotic Plant Collection",
                "description": "Unique and exotic plants to add a touch of the extraordinary to your space.",
                "budget_range": "$300 - $900",
            },
            {
                "id": 17,
                "title": "Meditation Garden",
                "description": "Create a serene space for meditation with our specialized plant decor services.",
                "budget_range": "$400 - $1200",
            },
            {
                "id": 18,
                "title": "Plant Styling Consultation",
                "description": "Personalized plant styling services to help you choose the perfect plants for your space.",
                "budget_range": "$100 - $300",
            },
            {
                "id": 19,
                "title": "Edible Garden",
                "description": "Grow your own herbs and vegetables with our edible garden decor services.",
                "budget_range": "$200 - $600",
            },
            {
                "id": 20,
                "title": "Terrarium Creations",
                "description": "Custom terrariums to bring a piece of nature indoors.",
                "budget_range": "$50 - $200",
            },
        ]

        # Get all categories and types
        categories = list(ServiceCategory.objects.all())
        types = list(ServiceType.objects.all())

        for entry in data:
            # Assign random category and type
            category = random.choice(categories)
            type_ = random.choice(types)

            Service.objects.get_or_create(
                title=entry["title"],
                defaults={
                    "description": entry["description"],
                    "budget_range": entry["budget_range"],
                    "category": category,
                    "type": type_,
                },
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with service data")
        )
