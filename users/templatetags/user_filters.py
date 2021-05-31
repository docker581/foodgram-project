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
def isPurchase(purchase, user):
    return Purchase.objects.filter(user=user, purchase=purchase).exists()


@register.filter
def countRestRecipes(total_number, specified_number):
    return total_number - specified_number


@register.filter
def tagLink(request, tag):
    request_copy = request.GET.copy()
    request_copy["page"] = "1"
    tags = request_copy.getlist("tags")
    if tag.slug in tags:
        tags.remove(tag.slug)
        request_copy.setlist("tags", tags)
    else:
        request_copy.appendlist("tags", tag.slug)
    return request_copy.urlencode()    
