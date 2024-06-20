# main/management/commands/seed_ideas.py

import os
from django.core.management.base import BaseCommand
from main.models import Ideas


class Command(BaseCommand):
    help = "Populate the database with idea data"

    def handle(self, *args, **kwargs):
        ideas_data = [
            {
                "title": "Vertical Garden",
                "description": "A beautiful vertical garden setup for urban homes.",
                "image": None,
                "tags": ["garden", "urban", "vertical"],
            },
            {
                "title": "Indoor Herb Planter",
                "description": "A compact indoor planter for growing herbs.",
                "image": None,
                "tags": ["indoor", "herbs", "compact"],
            },
            {
                "title": "Hanging Succulents",
                "description": "An aesthetic way to hang succulent plants in your home.",
                "image": None,
                "tags": ["succulents", "hanging", "decor"],
            },
            {
                "title": "Self-Watering Pot",
                "description": "A self-watering pot to keep your plants hydrated.",
                "image": None,
                "tags": ["self-watering", "pot", "hydration"],
            },
            {
                "title": "Outdoor Planter Bench",
                "description": "A dual-purpose bench with integrated planters.",
                "image": None,
                "tags": ["outdoor", "bench", "planter"],
            },
        ]

        for idea_data in ideas_data:
            idea, created = Ideas.objects.get_or_create(
                title=idea_data["title"],
                defaults={
                    "description": idea_data["description"],
                    "image": idea_data["image"],
                },
            )
            if created:
                idea.tags.add(*idea_data["tags"])

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with idea data")
        )
