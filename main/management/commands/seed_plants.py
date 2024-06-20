from django.core.management.base import BaseCommand
from main.models import PlantCategory, PlantFeatures, Plant


class Command(BaseCommand):
    help = "Seed data for PlantCategory, Features, and Plant models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        self.seed_plant_categories()
        self.seed_features()
        self.seed_plants()

        self.stdout.write(self.style.SUCCESS("Data seeding complete."))

    def seed_plant_categories(self):
        categories = [
            {"name": "Flowering Plants", "description": "Plants that produce flowers."},
            {
                "name": "Succulents",
                "description": "Plants that store water in their leaves.",
            },
            {
                "name": "Ferns",
                "description": "Non-flowering plants with feathery leaves.",
            },
            {"name": "Cacti", "description": "Plants with spines instead of leaves."},
            {"name": "Orchids", "description": "Flowering plants with unique blooms."},
            {"name": "Shrubs", "description": "Small to medium-sized woody plants."},
            {
                "name": "Trees",
                "description": "Tall woody plants with a single main stem.",
            },
            {"name": "Grasses", "description": "Plants with long, narrow leaves."},
            {
                "name": "Herbs",
                "description": "Plants used for culinary or medicinal purposes.",
            },
            {"name": "Vegetables", "description": "Edible plants grown in gardens."},
            {"name": "Fruits", "description": "Plants that produce fruits."},
        ]

        for category_data in categories:
            PlantCategory.objects.get_or_create(
                name=category_data["name"], defaults=category_data
            )

    def seed_features(self):
        features = [
            {"name": "Easy Care"},
            {"name": "Pet Friendly"},
            {"name": "Fragrant"},
            {"name": "Low Maintenance"},
            {"name": "Air Purifying"},
        ]

        for feature_data in features:
            PlantFeatures.objects.get_or_create(name=feature_data["name"])

    def seed_plants(self):
        plants = [
            {
                "title": "Rose",
                "category_name": "Flowering Plants",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A beautiful flowering plant with thorny stems.",
                "care_instructions": "Regular watering and pruning required.",
                "features": ["Fragrant"],
                "tags": "rose, flowering, garden",
            },
            {
                "title": "Aloe Vera",
                "category_name": "Succulents",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A succulent plant known for its medicinal properties.",
                "care_instructions": "Water sparingly, needs plenty of sunlight.",
                "features": ["Low Maintenance"],
                "tags": "aloe vera, succulent, indoor",
            },
            {
                "title": "Boston Fern",
                "category_name": "Ferns",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A popular houseplant with feathery fronds.",
                "care_instructions": "Needs high humidity and indirect sunlight.",
                "features": ["Air Purifying"],
                "tags": "boston fern, fern, indoor",
            },
            {
                "title": "Barrel Cactus",
                "category_name": "Cacti",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A small cactus with a barrel-like shape.",
                "care_instructions": "Water sparingly, needs plenty of sunlight.",
                "features": ["Pet Friendly"],
                "tags": "barrel cactus, cactus, outdoor",
            },
            {
                "title": "Phalaenopsis Orchid",
                "category_name": "Orchids",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A beautiful orchid with large, colorful blooms.",
                "care_instructions": "Requires high humidity and indirect sunlight.",
                "features": ["Fragrant"],
                "tags": "phalaenopsis orchid, orchid, indoor",
            },
            {
                "title": "Boxwood",
                "category_name": "Shrubs",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A versatile shrub with dense foliage.",
                "care_instructions": "Regular pruning required.",
                "features": ["Easy Care"],
                "tags": "boxwood, shrub, outdoor",
            },
            {
                "title": "Maple Tree",
                "category_name": "Trees",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A tall tree with colorful autumn foliage.",
                "care_instructions": "Needs plenty of sunlight and water.",
                "features": ["Air Purifying"],
                "tags": "maple tree, tree, outdoor",
            },
            {
                "title": "Bamboo",
                "category_name": "Grasses",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A fast-growing grass with tall, hollow stems.",
                "care_instructions": "Requires regular watering and pruning.",
                "features": ["Air Purifying"],
                "tags": "bamboo, grass, outdoor",
            },
            {
                "title": "Basil",
                "category_name": "Herbs",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A fragrant herb used in cooking and medicine.",
                "care_instructions": "Needs plenty of sunlight and well-drained soil.",
                "features": ["Easy Care"],
                "tags": "basil, herb, outdoor",
            },
            {
                "title": "Tomato",
                "category_name": "Vegetables",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A popular vegetable plant with juicy red fruits.",
                "care_instructions": "Requires regular watering and fertilizing.",
                "features": ["Pet Friendly"],
                "tags": "tomato, vegetable, outdoor",
            },
            {
                "title": "Apple Tree",
                "category_name": "Fruits",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A fruit tree with sweet, crunchy apples.",
                "care_instructions": "Needs plenty of sunlight and water.",
                "features": ["Air Purifying"],
                "tags": "apple tree, fruit, outdoor",
            },
            {
                "title": "Lavender",
                "category_name": "Flowering Plants",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A fragrant plant with purple flowers.",
                "care_instructions": "Requires well-drained soil and plenty of sunlight.",
                "features": ["Fragrant"],
                "tags": "lavender, flowering, garden",
            },
            {
                "title": "Jade Plant",
                "category_name": "Succulents",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A small succulent plant with thick, fleshy leaves.",
                "care_instructions": "Water sparingly, needs plenty of sunlight.",
                "features": ["Low Maintenance"],
                "tags": "jade plant, succulent, indoor",
            },
            {
                "title": "Bird's Nest Fern",
                "category_name": "Ferns",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A unique fern with crinkled, nest-like fronds.",
                "care_instructions": "Needs high humidity and indirect sunlight.",
                "features": ["Air Purifying"],
                "tags": "bird's nest fern, fern, indoor",
            },
            {
                "title": "Prickly Pear Cactus",
                "category_name": "Cacti",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A small cactus with flat, paddle-shaped stems.",
                "care_instructions": "Water sparingly, needs plenty of sunlight.",
                "features": ["Pet Friendly"],
                "tags": "prickly pear cactus, cactus, outdoor",
            },
            {
                "title": "Moth Orchid",
                "category_name": "Orchids",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A popular orchid with delicate, moth-like blooms.",
                "care_instructions": "Requires high humidity and indirect sunlight.",
                "features": ["Fragrant"],
                "tags": "moth orchid, orchid, indoor",
            },
            {
                "title": "Hydrangea",
                "category_name": "Shrubs",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A flowering shrub with large, colorful blooms.",
                "care_instructions": "Regular pruning required.",
                "features": ["Easy Care"],
                "tags": "hydrangea, shrub, outdoor",
            },
            {
                "title": "Pine Tree",
                "category_name": "Trees",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A tall tree with needle-like leaves.",
                "care_instructions": "Needs plenty of sunlight and water.",
                "features": ["Air Purifying"],
                "tags": "pine tree, tree, outdoor",
            },
            {
                "title": "Pampas Grass",
                "category_name": "Grasses",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A large grass with feathery plumes.",
                "care_instructions": "Requires regular watering and pruning.",
                "features": ["Air Purifying"],
                "tags": "pampas grass, grass, outdoor",
            },
            {
                "title": "Mint",
                "category_name": "Herbs",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A fragrant herb used in cooking and beverages.",
                "care_instructions": "Needs plenty of sunlight and well-drained soil.",
                "features": ["Easy Care"],
                "tags": "mint, herb, outdoor",
            },
            {
                "title": "Bell Pepper",
                "category_name": "Vegetables",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A popular vegetable plant with colorful bell peppers.",
                "care_instructions": "Requires regular watering and fertilizing.",
                "features": ["Pet Friendly"],
                "tags": "bell pepper, vegetable, outdoor",
            },
            {
                "title": "Orange Tree",
                "category_name": "Fruits",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.LARGE,
                "description": "A fruit tree with sweet, juicy oranges.",
                "care_instructions": "Needs plenty of sunlight and water.",
                "features": ["Air Purifying"],
                "tags": "orange tree, fruit, outdoor",
            },
            {
                "title": "Daisy",
                "category_name": "Flowering Plants",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A cheerful flowering plant with white petals.",
                "care_instructions": "Regular watering and pruning required.",
                "features": ["Fragrant"],
                "tags": "daisy, flowering, garden",
            },
            {
                "title": "Snake Plant",
                "category_name": "Succulents",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A low-maintenance succulent plant with tall, upright leaves.",
                "care_instructions": "Water sparingly, needs plenty of sunlight.",
                "features": ["Low Maintenance"],
                "tags": "snake plant, succulent, indoor",
            },
            {
                "title": "Asparagus Fern",
                "category_name": "Ferns",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A fern with delicate, lacy foliage.",
                "care_instructions": "Needs high humidity and indirect sunlight.",
                "features": ["Air Purifying"],
                "tags": "asparagus fern, fern, indoor",
            },
            {
                "title": "Golden Barrel Cactus",
                "category_name": "Cacti",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.OUTDOOR,
                "size": Plant.SizeChoices.SMALL,
                "description": "A small cactus with golden spines.",
                "care_instructions": "Water sparingly, needs plenty of sunlight.",
                "features": ["Pet Friendly"],
                "tags": "golden barrel cactus, cactus, outdoor",
            },
            {
                "title": "Lady's Slipper Orchid",
                "category_name": "Orchids",
                "indoor_or_outdoor": Plant.IndoorOutdoorChoices.INDOOR,
                "size": Plant.SizeChoices.MEDIUM,
                "description": "A rare orchid with slipper-shaped blooms.",
                "care_instructions": "Requires high humidity and indirect sunlight.",
                "features": ["Fragrant"],
                "tags": "lady's slipper orchid, orchid, indoor",
            },
        ]

        for plant_data in plants:
            category_name = plant_data.pop("category_name")
            category = PlantCategory.objects.get(name=category_name)

            features = plant_data.pop("features")
            feature_objs = PlantFeatures.objects.filter(name__in=features)

            plant_data["category"] = category

            # Create or update the plant instance
            plant, created = Plant.objects.update_or_create(
                title=plant_data["title"],
                category=category,
                defaults=plant_data,
            )

            plant.features.set(feature_objs)
