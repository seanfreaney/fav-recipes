from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import RecipeForm, RecipeIngredientForm, RecipeCategoryForm

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe_list.html"
    paginate_by = 4


def recipe_detail(request, pk):
   # queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(Recipe, pk=pk)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )


def create_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        ingredient_form = RecipeIngredientForm(request.POST)
        category_form = RecipeCategoryForm(request.POST)

        if recipe_form.is_valid() and ingredient_form.is_valid() and category_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user 
            recipe.save()
            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            category = category_form.save(commit=False)
            category.recipe = recipe
            category.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        recipe_form = RecipeForm()
        ingredient_form = RecipeIngredientForm()
        category_form = RecipeCategoryForm()

    return render(request, "recipes/create_recipe.html", {
        "recipe_form": recipe_form,
        "ingredient_form": ingredient_form,
        "category_form": category_form,
    })