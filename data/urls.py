from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_recipe, name='new_recipe'),
    path(
        'recipe/<slug:recipe_slug>/', 
        views.recipe_detail, 
        name='recipe_detail',
    ),
    path('favorite/', views.favorite, name='favorite'),
    path('<str:username>/', views.profile, name='profile'), 
]