# recipes/forms.py

from django import forms
from django.forms import inlineformset_factory
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

RecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, form=RecipeIngredientForm, extra=1, can_delete=True)
