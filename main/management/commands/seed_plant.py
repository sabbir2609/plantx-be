import random
from django.core.management.base import BaseCommand
from main.models import Plant, PlantCategory, PlantFeatures, Promotion


class Command(BaseCommand):
    help = "Populate the database with 10 example plants"

    def handle(self, *args, **kwargs):
        plant_data = [
            {
                "name": "Aloe Vera",
                "description": "Aloe Vera is a succulent plant species of the genus Aloe.",
                "care_instructions": "Water deeply but infrequently. Needs bright, indirect light.",
                "inventory": 10,
            },
            {
                "name": "Spider Plant",
                "description": "Spider Plant is known for its air-purifying properties.",
                "care_instructions": "Water regularly to keep the soil slightly moist. Needs bright, indirect light.",
                "inventory": 15,
            },
            {
                "name": "Peace Lily",
                "description": "Peace Lily is a popular indoor plant with white flowers.",
                "care_instructions": "Water regularly, allowing the soil to dry out between waterings. Prefers low to bright light.",
                "inventory": 20,
            },
            {
                "name": "Fiddle Leaf Fig",
                "description": "Fiddle Leaf Fig has large, wavy leaves and is a favorite among interior designers.",
                "care_instructions": "Water when the top inch of soil is dry. Needs bright, indirect light.",
                "inventory": 5,
            },
            {
                "name": "Snake Plant",
                "description": "Snake Plant is a hardy plant that can tolerate low light and irregular watering.",
                "care_instructions": "Water when the soil is dry. Tolerates low to bright, indirect light.",
                "inventory": 25,
            },
            {
                "name": "Boston Fern",
                "description": "Boston Fern has lush, feathery fronds and prefers high humidity.",
                "care_instructions": "Keep the soil consistently moist. Prefers high humidity and indirect light.",
                "inventory": 12,
            },
            {
                "name": "Bamboo Palm",
                "description": "Bamboo Palm is a tropical plant that adds a touch of the exotic to any room.",
                "care_instructions": "Water when the top inch of soil is dry. Needs bright, indirect light.",
                "inventory": 18,
            },
            {
                "name": "Jade Plant",
                "description": "Jade Plant is a succulent known for its fleshy, oval-shaped leaves.",
                "care_instructions": "Water when the soil is dry. Needs bright, indirect light.",
                "inventory": 30,
            },
            {
                "name": "Pothos",
                "description": "Pothos is an easy-to-grow plant with heart-shaped leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Can tolerate low to bright, indirect light.",
                "inventory": 22,
            },
            {
                "name": "ZZ Plant",
                "description": "ZZ Plant is almost indestructible and perfect for low-light conditions.",
                "care_instructions": "Water when the soil is dry. Tolerates low to bright, indirect light.",
                "inventory": 16,
            },
            {
                "name": "Rubber Plant",
                "description": "Rubber Plant is a popular indoor plant with large, glossy leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Needs bright, indirect light.",
                "inventory": 8,
            },
            {
                "name": "Monstera",
                "description": "Monstera is a tropical plant with large, perforated leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Needs bright, indirect light.",
                "inventory": 14,
            },
            {
                "name": "Philodendron",
                "description": "Philodendron is a popular indoor plant with heart-shaped leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Can tolerate low to bright, indirect light.",
                "inventory": 11,
            },
            {
                "name": "Calathea",
                "description": "Calathea is known for its striking, patterned leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 9,
            },
            {
                "name": "Parlor Palm",
                "description": "Parlor Palm is a popular houseplant with delicate, feathery fronds.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 13,
            },
            {
                "name": "Areca Palm",
                "description": "Areca Palm is a tropical plant with feathery, arching fronds.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 7,
            },
            {
                "name": "Chinese Evergreen",
                "description": "Chinese Evergreen is a popular houseplant with variegated leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Can tolerate low to bright, indirect light.",
                "inventory": 6,
            },
            {
                "name": "African Violet",
                "description": "African Violet is a flowering plant with fuzzy leaves and colorful flowers.",
                "care_instructions": "Water from the bottom to keep the leaves dry. Prefers bright, indirect light.",
                "inventory": 4,
            },
            {
                "name": "Anthurium",
                "description": "Anthurium is a tropical plant with glossy, heart-shaped leaves and red flowers.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 3,
            },
            {
                "name": "Bird of Paradise",
                "description": "Bird of Paradise is a tropical plant with large, banana-like leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Needs bright, indirect light.",
                "inventory": 2,
            },
            {
                "name": "Croton",
                "description": "Croton is a colorful plant with variegated leaves in shades of red, orange, and yellow.",
                "care_instructions": "Water when the top inch of soil is dry. Needs bright, indirect light.",
                "inventory": 1,
            },
            {
                "name": "Dracaena",
                "description": "Dracaena is a popular house plant with long, sword-shaped leaves.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 17,
            },
            {
                "name": "Fern",
                "description": "Fern is a classic houseplant with delicate, lacy fronds.",
                "care_instructions": "Keep the soil consistently moist. Prefers high humidity and indirect light.",
                "inventory": 19,
            },
            {
                "name": "Ivy",
                "description": "Ivy is a trailing plant that can be grown indoors or outdoors.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 21,
            },
            {
                "name": "Lavender",
                "description": "Lavender is a fragrant herb with purple flowers.",
                "care_instructions": "Water when the soil is dry. Needs full sun.",
                "inventory": 23,
            },
            {
                "name": "Mint",
                "description": "Mint is a fragrant herb that is easy to grow indoors or outdoors.",
                "care_instructions": "Keep the soil consistently moist. Prefers full sun.",
                "inventory": 24,
            },
            {
                "name": "Orchid",
                "description": "Orchid is a flowering plant with elegant, exotic blooms.",
                "care_instructions": "Water when the top inch of soil is dry. Prefers bright, indirect light.",
                "inventory": 26,
            },
            {
                "name": "Rosemary",
                "description": "Rosemary is a fragrant herb with needle-like leaves.",
                "care_instructions": "Water when the soil is dry. Needs full sun.",
                "inventory": 27,
            },
            {
                "name": "Succulent",
                "description": "Succulent is a low-maintenance plant that stores water in its leaves.",
                "care_instructions": "Water sparingly. Needs bright, indirect light.",
                "inventory": 28,
            },
            {
                "name": "Thyme",
                "description": "Thyme is a fragrant herb with tiny, aromatic leaves.",
                "care_instructions": "Water when the soil is dry. Prefers full sun.",
                "inventory": 29,
            },
        ]

        categories = list(PlantCategory.objects.all())
        features = list(PlantFeatures.objects.all())
        promotions = list(Promotion.objects.all())

        sizes = ["Small", "Medium", "Large", "Extra Large"]
        location_types = ["Indoor", "Outdoor", "Both"]

        for plant_info in plant_data:
            category = random.choice(categories)
            plant, created = Plant.objects.get_or_create(
                name=plant_info["name"],
                defaults={
                    "size": random.choice(sizes),
                    "unit_price": random.randint(100, 1000),
                    "category": category,
                    "location_type": random.choice(location_types),
                    "description": plant_info["description"],
                    "care_instructions": plant_info["care_instructions"],
                    "inventory": plant_info["inventory"],
                },
            )

            if created:
                selected_features = random.sample(
                    features, k=random.randint(1, len(features))
                )
                for feature in selected_features:
                    plant.features.add(feature)

                selected_promotions = random.sample(
                    promotions, k=random.randint(1, len(promotions))
                )
                for promotion in selected_promotions:
                    plant.promotion.add(promotion)

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created plant: {plant.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Plant already exists: {plant.name}")
                )
