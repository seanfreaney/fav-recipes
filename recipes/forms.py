# recipes/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeIngredient, RecipeCategory, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'status']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ingredient'].queryset = Ingredient.objects.all().order_by('name')

class RecipeCategoryForm(forms.ModelForm):
    class Meta:
        model = RecipeCategory
        fields = ['category']

RecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, form=RecipeIngredientForm, extra=1, can_delete=True)
