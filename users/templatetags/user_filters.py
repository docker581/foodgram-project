from django import template

from data.models import Favorite, Subscription

register = template.Library()


@register.filter 
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def findIngredient(ingredients, ingredient):
    return ingredients.filter(ingredient=ingredient)


@register.filter
def isFavorite(recipe, user):
    return Favorite.objects.filter(user=user, recipe=recipe).exists()


@register.filter
def isSubscription(author, user):
    return Subscription.objects.filter(author=author, user=user).exists()    
