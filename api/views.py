from django.http import JsonResponse

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

SUCCESS = JsonResponse({'success': True})
FAILURE = JsonResponse({'success': False}, status=status.HTTP_400_BAD_REQUEST)


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        ingredient = self.request.query_params.get('query')
        if ingredient is not None:
            queryset = queryset.filter(name__startswith=ingredient)
        return queryset


class AddEssenceAPIView(views.APIView):
    def post(self, request, format=None):
        pass


class AddFavoriteAPIView(views.APIView):
    def post(self, request, format=None):
        recipe = Recipe.objects.get(id=request.data['id'])
        if Favorite.objects.create(user=request.user, recipe=recipe):
            return SUCCESS
        else:
            return FAILURE


class RemoveFavoriteAPIView(views.APIView):
    def delete(self, request, id, format=None):
        recipe = Recipe.objects.get(id=id)
        if Favorite.objects.filter(recipe=recipe, user=request.user).delete():
            return SUCCESS
        else:
            return FAILURE


class AddSubscriptionAPIView(views.APIView):
    def post(self, request, format=None):
        author = User.objects.get(id=request.data['id'])
        if author != request.user:
            if Subscription.objects.create(author=author, user=request.user):
                return SUCCESS
            else:
                return FAILURE
        return FAILURE


class RemoveSubscriptionAPIView(views.APIView):
    def delete(self, request, id, format=None):
        author = User.objects.get(id=id)
        if Subscription.objects.filter(
            author=author, user=request.user,
        ).delete():
            return SUCCESS
        else:
            return FAILURE


class PurchaseAPIView(views.APIView):
    def get(self, request, format=None):
        purchases = Purchase.objects.all()
        return response.Response(
            {'success': True},
            data=purchases,
            status=status.HTTP_200_OK,
        )

    def post(self, request, format=None):
        purchase = Recipe.objects.get(id=request.data['id'])
        if Purchase.objects.create(user=request.user, purchase=purchase):
            return SUCCESS
        else:
            return FAILURE


class RemovePurchaseAPIView(views.APIView):
    def delete(self, request, id, format=None):
        purchase = Recipe.objects.get(id=id)
        if Purchase.objects.filter(
            purchase=purchase, user=request.user,
        ).delete():
            return SUCCESS
        else:
            return FAILURE
