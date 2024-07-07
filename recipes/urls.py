from . import views
from django.urls import path, include


urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]