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
    path(
        'recipe/<slug:recipe_slug>/edit/', 
        views.recipe_edit, 
        name='recipe_edit',
    ),
    path('favorites/', views.favorites, name='favorites'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('author/', views.AboutAuthorView.as_view(), name='author'),
    path('tech/', views.AboutTechView.as_view(), name='tech'),
    path('<str:username>/', views.profile, name='profile'), 
]