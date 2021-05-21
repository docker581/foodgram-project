from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    IngredientViewSet, 
    AddFavoritesAPIView, 
    RemoveFavoritesAPIView,
)

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]
urlpatterns += [
    path(
        'v1/favorites', 
        AddFavoritesAPIView.as_view(), 
    ),
    path(
        'v1/favorites/<int:id>', 
        RemoveFavoritesAPIView.as_view(), 
    ),
]