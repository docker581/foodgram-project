from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    IngredientViewSet,
    FavoriteAPIView,
    SubscriptionAPIView,
    PurchaseAPIView,
)

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]
urlpatterns += [
    path('v1/favorites', FavoriteAPIView.as_view()),
    path('v1/favorites/<int:id>', FavoriteAPIView.as_view()),
    path('v1/subscriptions', SubscriptionAPIView.as_view()),
    path('v1/subscriptions/<int:id>', SubscriptionAPIView.as_view()),
    path('v1/purchases', PurchaseAPIView.as_view()),
    path('v1/purchases/<int:id>', PurchaseAPIView.as_view()),
]
