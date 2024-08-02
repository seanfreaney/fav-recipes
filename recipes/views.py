from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from .models import Recipe, Category
from .forms import RecipeForm, RecipeIngredientFormSet, RecipeCategoryForm

# Create your views here.


class RecipeList(generic.ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 4

    def get_queryset(self):
        queryset = Recipe.objects.all()
        category = self.request.GET.get("category")
        sort_by = self.request.GET.get("sort_by")
        search_query = self.request.GET.get("q")

        if category:
            queryset = queryset.filter(categories__name__icontains=category)

        if sort_by == "newest":
            queryset = queryset.order_by("-created_on")
        elif sort_by == "oldest":
            queryset = queryset.order_by("created_on")

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(description__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sort_by'] = self.request.GET.get("sort_by", "")
        context['search_query'] = self.request.GET.get("q", "")
        return context


def recipe_detail(request, pk):
    # queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(Recipe, pk=pk)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )


@login_required
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
            messages.success(request, 'Recipe created successfully!')
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


@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(
            request.POST, request.FILES, instance=recipe)
        category_form = RecipeCategoryForm(
            request.POST, instance=recipe.recipecategory_set.first())

        if recipe_form.is_valid() and ingredient_formset.is_valid(

        ) and category_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            ingredient_formset.instance = recipe
            ingredient_formset.save()
            category = category_form.save(commit=False)
            category.recipe = recipe
            category.save()
            messages.success(request, 'Recipe updated successfully!')
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(instance=recipe)
        category_form = RecipeCategoryForm(
            instance=recipe.recipecategory_set.first())

    return render(request, "recipes/edit_recipe.html", {
        "recipe_form": recipe_form,
        "ingredient_formset": ingredient_formset,
        "category_form": category_form,
    })


@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == "POST":
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
        return redirect('home')
    return render(request, 'recipes/confirm_delete.html', {'recipe': recipe})
