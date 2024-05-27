from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from .models import Plant, Category

from blog.models import Post


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_plants"] = Plant.objects.all()[
            :3
        ]  # Get top 3 featured plants
        context["popular_categories"] = Category.objects.all()[
            :3
        ]  # Get top 3 categories
        context["recent_posts"] = Post.objects.all()[:3]  # Get top 3 recent blog posts
        return context


class CategoryListView(ListView):
    model = Category
    template_name = "main/category_list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "main/category_detail.html"
    context_object_name = "category"


class PlantListView(ListView):
    model = Plant
    template_name = "main/plant_list.html"
    context_object_name = "plants"


class PlantDetailView(DetailView):
    model = Plant
    template_name = "main/plant_detail.html"
    context_object_name = "plant"
