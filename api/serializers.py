from rest_framework import serializers

from data.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'dimension']
        model = Ingredient
