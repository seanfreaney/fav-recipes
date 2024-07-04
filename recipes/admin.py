from django.contrib import admin
from .models import Category, Ingredient, Recipe, RecipeIngredient, RecipeCategory

# Inline model for RecipeIngredient
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # Number of extra empty forms to display

# Inline model for RecipeCategory
class RecipeCategoryInline(admin.TabularInline):
    model = RecipeCategory
    extra = 1  # Number of extra empty forms to display

# Admin model for Recipe
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeCategoryInline]

# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeCategory)
