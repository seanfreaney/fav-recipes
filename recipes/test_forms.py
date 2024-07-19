from django.test import TestCase
from recipes.forms import RecipeForm, RecipeIngredientForm, RecipeCategoryForm
from recipes.models import Recipe, Ingredient, Category

class RecipeFormTest(TestCase):

    def test_valid_recipe_form(self):
        form_data = {
            'title': 'Test Recipe',
            'description': 'Test Description',
            'instructions': 'Test Instructions',
            'status': 1,
        }
        form = RecipeForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_recipe_form(self):
        form_data = {
            'title': '',
            'description': 'Test Description',
            'instructions': 'Test Instructions',
            'status': 1,
        }
        form = RecipeForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_recipe_form_fields(self):
        form = RecipeForm()
        self.assertIn('title', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('instructions', form.fields)
        self.assertIn('status', form.fields)


class RecipeIngredientFormTest(TestCase):

    def setUp(self):
        self.ingredient = Ingredient.objects.create(name='Test Ingredient')

    def test_valid_ingredient_form(self):
        form_data = {
            'ingredient': self.ingredient.id,
            'quantity': 1,
        }
        form = RecipeIngredientForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_ingredient_form(self):
        form_data = {
            'ingredient': '',
            'quantity': 1,
        }
        form = RecipeIngredientForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_ingredient_queryset(self):
        form = RecipeIngredientForm()
        self.assertQuerysetEqual(
            form.fields['ingredient'].queryset,
            Ingredient.objects.all().order_by('name')
        )


class RecipeCategoryFormTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_valid_category_form(self):
        form_data = {
            'category': self.category.id,
        }
        form = RecipeCategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_category_form(self):
        form_data = {
            'category': '',
        }
        form = RecipeCategoryForm(data=form_data)
        self.assertFalse(form.is_valid())