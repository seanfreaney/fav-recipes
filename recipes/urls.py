from . import views
from django.urls import path, include


urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.RecipeList.as_view(), name='home'),
    path("accounts/", include("allauth.urls")),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/create/', views.create_recipe, name='create_recipe'),
    path('recipe/<int:pk>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
]