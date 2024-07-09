# recipes/forms.py

from django import forms
from .models import Recipe, RecipeIngredient, RecipeCategory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'status']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class RecipeCategoryForm(forms.ModelForm):
    class Meta:
        model = RecipeCategory
        fields = ['category']
