from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe, Category, Ingredient, RecipeIngredient, RecipeCategory

class RecipeDetailViewTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create category
        self.category1 = Category.objects.create(pk=1)

        # Create ingredients
        self.ingredient1 = Ingredient.objects.create(pk=2)
        self.ingredient2 = Ingredient.objects.create(pk=3)

        # Create a published recipe
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='This is a test recipe',
            instructions='Mix ingredients and bake.',
            user=self.user,
            status=1
        )

        # Associate categories and ingredients with the recipe
        RecipeCategory.objects.create(recipe=self.recipe, category=self.category1)
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient1, quantity='1 cup')
        RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient2, quantity='2 cups')

        self.client = Client()

    def test_recipe_detail_view_with_published_recipe(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')
        self.assertContains(response, self.recipe.title)
        self.assertContains(response, self.recipe.description)
        self.assertContains(response, self.ingredient1.name)
        self.assertContains(response, self.ingredient2.name)

    # to be run once draft posting available to user
    # def test_recipe_detail_view_with_draft_recipe(self):
    #    response = self.client.get(reverse('recipe_detail', args=[self.draft_recipe.pk]))
    #    self.assertEqual(response.status_code, 404)
    