from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    IngredientViewSet,
    AddFavoriteAPIView,
    RemoveFavoriteAPIView,
    AddSubscriptionAPIView,
    RemoveSubscriptionAPIView,
    PurchaseAPIView,
    RemovePurchaseAPIView,
)

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]
urlpatterns += [
    path('v1/favorites', AddFavoriteAPIView.as_view()),
    path('v1/favorites/<int:id>', RemoveFavoriteAPIView.as_view()),
    path('v1/subscriptions', AddSubscriptionAPIView.as_view()),
    path('v1/subscriptions/<int:id>', RemoveSubscriptionAPIView.as_view()),
    path('v1/purchases', PurchaseAPIView.as_view()),
    path('v1/purchases/<int:id>', RemovePurchaseAPIView.as_view()),
]
