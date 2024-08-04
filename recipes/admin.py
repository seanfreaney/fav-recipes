from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
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
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    inlines = [RecipeIngredientInline, RecipeCategoryInline]
    list_display = ('title', 'description', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    summernote_fields = ('instructions',)


# Register your models here.
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeCategory)
