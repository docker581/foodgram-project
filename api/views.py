from rest_framework import mixins, viewsets, views, status, response

from data.models import (
    User, 
    Ingredient, 
    Recipe, 
    Favorite, 
    Subscription, 
    Purchase,
)
from .serializers import IngredientSerializer


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        ingredient = self.request.query_params.get('query')
        if ingredient is not None:
            queryset = queryset.filter(name__startswith=ingredient)
        return queryset


class AddFavoriteAPIView(views.APIView):
    def post(self, request, format=None):
        recipe = Recipe.objects.get(id=request.data['id'])
        Favorite.objects.get_or_create(
            user=request.user,
            recipe=recipe,
        )
        return response.Response({'success': True}, status=status.HTTP_200_OK)


class RemoveFavoriteAPIView(views.APIView):
    def delete(self, request, id, format=None):
        recipe = Recipe.objects.get(id=id)
        Favorite.objects.filter(recipe=recipe, user=request.user).delete()
        return response.Response({'success': True}, status=status.HTTP_200_OK)


class AddSubscriptionAPIView(views.APIView):
    def post(self, request, format=None):
        author = User.objects.get(id=request.data['id'])
        if author != request.user:
            Subscription.objects.get_or_create(
                author = author,
                user=request.user,
            )
        return response.Response({'success': True}, status=status.HTTP_200_OK)


class RemoveSubscriptionAPIView(views.APIView):
    def delete(self, request, id, format=None):
        author = User.objects.get(id=id)
        Subscription.objects.filter(author=author, user=request.user).delete()
        return response.Response({'success': True}, status=status.HTTP_200_OK) 


class PurchaseAPIView(views.APIView):
    def post(self, request, format=None):
        purchases_number = Purchase.objects.count()
        return response.Response({'success': True}, data=purchases_number, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        purchase = Purchase.objects.get(id=request.data['id'])
        Purchase.objects.get_or_create(
            user=request.user,
            purchase=purchase,
        )
        return response.Response({'success': True}, status=status.HTTP_200_OK)


class RemovePurchaseAPIView(views.APIView):
    def delete(self, request, id, format=None):
        purchase = Purchase.objects.get(id=id)
        Purchase.objects.filter(purchase=purchase, user=request.user).delete()
        return response.Response({'success': True}, status=status.HTTP_200_OK)
