from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipe_list.html"
    paginate_by = 4


def recipe_detail(request, pk):
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )