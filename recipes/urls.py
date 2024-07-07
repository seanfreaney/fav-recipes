from . import views
from django.urls import path, include


urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('', views.RecipeList.as_view(), name='home'),
]