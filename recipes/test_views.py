from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe, Category, Ingredient, RecipeIngredient, RecipeCategory
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


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


class RecipeListViewTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Create a category
        self.category1 = Category.objects.create(pk=2)

        #Create ingredients
        self.ingredient1 = Ingredient.objects.create(pk=15)
        self.ingredient2 = Ingredient.objects.create(pk=5)
        self.ingredient3 = Ingredient.objects.create(pk=25)

        # Create recipes
        self.recipe1 = Recipe.objects.create(
            title='Chocolate Cake',
            description='Delicious chocolate cake.',
            instructions='Bake the cake.',
            user=self.user,
            status=1,
            created_on=timezone.now() - timedelta(days=1)
        )
        self.recipe2 = Recipe.objects.create(
            title='Pancakes',
            description='Fluffy pancakes.',
            instructions='Cook the pancakes.',
            user=self.user,
            status=1,
            created_on=timezone.now()
        )
        self.recipe3 = Recipe.objects.create(
            title='Salad',
            description='Fresh salad.',
            instructions='Mix ingredients.',
            user=self.user,
            status=0,
            created_on=timezone.now()
        )

        # Associate categories with the recipes
        RecipeCategory.objects.create(recipe=self.recipe1, category=self.category1)
        RecipeCategory.objects.create(recipe=self.recipe2, category=self.category1)
        RecipeCategory.objects.create(recipe=self.recipe3, category=self.category1)

        # Associate ingredients with the recipes
        RecipeIngredient.objects.create(recipe=self.recipe1, ingredient=self.ingredient1, quantity='1 cup')
        RecipeIngredient.objects.create(recipe=self.recipe1, ingredient=self.ingredient2, quantity='2 cups')
        RecipeIngredient.objects.create(recipe=self.recipe2, ingredient=self.ingredient2, quantity='1 cup')
        RecipeIngredient.objects.create(recipe=self.recipe2, ingredient=self.ingredient3, quantity='3')
        RecipeIngredient.objects.create(recipe=self.recipe3, ingredient=self.ingredient2, quantity='1 cup')
        RecipeIngredient.objects.create(recipe=self.recipe3, ingredient=self.ingredient3, quantity='3')

        self.client = Client()


    def test_recipe_list_view_pagination(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')
        self.assertEqual(len(response.context['recipes']), 2)  

    def test_recipe_list_view_filter_by_category(self):
        response = self.client.get(reverse('home') + '?category=Lunch')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Chocolate Cake')  