from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Recipe
from .forms import RecipeForm, RecipeIngredientFormSet, RecipeCategoryForm

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
        ingredient_formset = RecipeIngredientFormSet(request.POST, request.FILES)
        category_form = RecipeCategoryForm(request.POST)

        if recipe_form.is_valid() and ingredient_formset.is_valid() and category_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            ingredient_formset.instance = recipe
            ingredient_formset.save()
            category = category_form.save(commit=False)
            category.recipe = recipe
            category.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()
        category_form = RecipeCategoryForm()

    return render(request, "recipes/create_recipe.html", {
        "recipe_form": recipe_form,
        "ingredient_formset": ingredient_formset,
        "category_form": category_form,
    })