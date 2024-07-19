from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe, Ingredient, Category


class RecipeListViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_recipe_list_view_with_filters(self):
        Recipe.objects.create(title='Recipe 1', description='Description', instructions='Instructions', status=1, user=self.user)
        Recipe.objects.create(title='Recipe 2', description='Description', instructions='Instructions', status=0, user=self.user)
        
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')
        self.assertContains(response, 'Recipe 1')
        self.assertNotContains(response, 'Recipe 2')

    def test_pagination(self):
        for i in range(30):
            Recipe.objects.create(title=f'Recipe {i}', description='Description', instructions='Instructions', status=1, user=self.user)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['recipe_list']), 10)