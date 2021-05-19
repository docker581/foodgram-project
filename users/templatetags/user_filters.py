from data.models import Ingredient
from django import template

register = template.Library()


@register.filter 
def addclass(field, css):
        return field.as_widget(attrs={"class": css})


@register.filter
def findIngredient(ingredients, ingredient):
    return ingredients.filter(ingredient=ingredient)
