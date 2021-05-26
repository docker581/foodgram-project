from django import template

from data.models import Favorite, Subscription, Purchase

register = template.Library()


@register.filter 
def addClass(field, classname):
    return field.as_widget(attrs={"class": classname})


@register.filter
def findIngredient(ingredients, ingredient):
    return ingredients.filter(ingredient=ingredient)


@register.filter
def isFavorite(recipe, user):
    return Favorite.objects.filter(user=user, recipe=recipe).exists()


@register.filter
def isSubscription(author, user):
    return Subscription.objects.filter(author=author, user=user).exists()    


@register.filter
def countRestRecipes(total_number, specified_number):
    return total_number - specified_number


@register.filter
def isPurchase(purchase, user):
    return Purchase.objects.filter(user=user, purchase=purchase).exists()     


from django.utils.safestring import mark_safe
@register.simple_tag(takes_context=True)
def urlReplace(context, **kwargs):
    query = context['request'].GET.copy()
    for kwarg in kwargs:
        try:
            query.pop(kwarg)
        except KeyError:
            pass
    query.update(kwargs)
    return mark_safe(query.urlencode())
