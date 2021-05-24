from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    IngredientViewSet, 
    AddFavoriteAPIView, 
    RemoveFavoriteAPIView,
    AddSubscriptAPIView, 
    RemoveSubscriptAPIView,
)

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]
urlpatterns += [
    path(
        'v1/favorites', 
        AddFavoriteAPIView.as_view(), 
    ),
    path(
        'v1/favorites/<int:id>', 
        RemoveFavoriteAPIView.as_view(), 
    ),
    path(
        'v1/subscriptions', 
        AddSubscriptAPIView.as_view(), 
    ),
    path(
        'v1/subscriptions/<int:id>', 
        RemoveSubscriptAPIView.as_view(), 
    ),
]