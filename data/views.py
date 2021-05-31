from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import (
    User,
    Tag,
    Ingredient,
    Recipe,
    RecipeIngredient,
    Subscription,
)
from .forms import RecipeForm


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404,
    )


def server_error(request):
    return render(request, "misc/500.html", status=500)


def index(request):
    common_tags = Tag.objects.all()
    get_tags = request.GET.getlist('tags')
    if get_tags:
        active_tags = Tag.objects.filter(slug__in=get_tags)
    else:
        active_tags = Tag.objects.all()          
    recipes = Recipe.objects.filter(tags__in=active_tags).distinct()
    paginator = Paginator(recipes, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {
            'common_tags': common_tags,
            'active_tags': active_tags,
            'page': page,
            'paginator': paginator,
        }
    )


def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            value_ingredient = key[15:]
            ingredients[request.POST[key]] = request.POST[
                'valueIngredient_' + value_ingredient
            ]
    return ingredients


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    ingredients = get_ingredients(request)
    if not form.is_valid():
        return render(
            request,
            'new.html',
            {
                'form': form,
                'page_title': 'Создание рецепта',
                'page_button': 'Создать рецепт',
            }
        )
    recipe = form.save(commit=False)
    recipe.author = request.user
    recipe.save()
    RecipeIngredient.objects.filter(recipe=recipe).delete()
    objects = []
    for name, quantity in ingredients.items():
        ingredient = get_object_or_404(Ingredient, name=name)
        objects.append(RecipeIngredient(
            recipe=recipe,
            ingredient=ingredient,
            quantity=quantity,
        ))
    RecipeIngredient.objects.bulk_create(objects)
    form.save_m2m()
    return redirect('index')


@login_required
def recipe_edit(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    if request.user != recipe.author:
        return redirect('detail', recipe_slug)
    form = RecipeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=recipe,
    )
    ingredients = get_ingredients(request)
    if request.method == 'POST':
        if form.is_valid():
            recipe = Recipe.objects.get(slug=recipe_slug)
            recipe.name = form.cleaned_data['name']
            recipe.time = form.cleaned_data['time']
            recipe.description = form.cleaned_data['description']
            recipe.image = form.cleaned_data['image']
            recipe.slug = form.cleaned_data['slug']
            recipe.save()
            recipe.tags.set(form.cleaned_data['tags'])
            RecipeIngredient.objects.filter(recipe=recipe).delete()
            objects = []
            for name, quantity in ingredients.items():
                ingredient = get_object_or_404(Ingredient, name=name)
                objects.append(RecipeIngredient(
                    recipe=recipe,
                    ingredient=ingredient,
                    quantity=quantity,
                ))
            RecipeIngredient.objects.bulk_create(objects)
            form.save()
            return redirect('recipe_detail', recipe_slug)
    return render(
        request,
        'new.html',
        {
            'form': form,
            'page_title': 'Изменение рецепта',
            'page_button': 'Редактировать рецепт',
        }
    )


def recipe_detail(request, recipe_slug):
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(
        request,
        'detail.html',
        {
            'recipe': recipe,
            'recipe_ingredients': recipe_ingredients,
        }
    )


def profile(request, username):
    common_tags = Tag.objects.all()
    get_tags = request.GET.getlist('tags')
    if get_tags:
        active_tags = Tag.objects.filter(slug__in=get_tags)
    else:
        active_tags = Tag.objects.all()
    author = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(author=author).filter(
        tags__in=active_tags,
    ).distinct()
    paginator = Paginator(recipes, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'profile.html',
        {
            'common_tags': common_tags,
            'active_tags': active_tags,
            'author': author,
            'page': page,
            'paginator': paginator,
        }
    )


@login_required
def favorites(request):
    common_tags = Tag.objects.all()
    get_tags = request.GET.getlist('tags')
    if get_tags:
        active_tags = Tag.objects.filter(slug__in=get_tags)
    else:
        active_tags = Tag.objects.all()
    favorites = Recipe.objects.filter(
        favorites__user=request.user,
    ).filter(tags__in=active_tags).distinct()
    paginator = Paginator(favorites, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'favorites.html',
        {
            'common_tags': common_tags,
            'active_tags': active_tags,
            'favorites': favorites,
            'page': page,
            'paginator': paginator,
        }
    )


@login_required
def subscriptions(request):
    subscriptions = Subscription.objects.filter(
        author__subscriptions__user=request.user,
    )
    paginator = Paginator(subscriptions, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'subscriptions.html',
        {
            'subscriptions': subscriptions,
            'page': page,
            'paginator': paginator,
        }
    )


@login_required
def purchases(request):
    purchases = Recipe.objects.filter(purchases__user=request.user)
    return render(
        request,
        'purchases.html',
        {
            'purchases': purchases,
        }
    )


@login_required
def download_ingredients(request):
    ingredients = RecipeIngredient.objects.filter(
        recipe__in=Recipe.objects.filter(
            purchases__user=request.user,
        )
    )
    dict_ = {}
    for ingredient in ingredients:
        key = (
            f'{ingredient.ingredient.name} '
            f'({ingredient.ingredient.dimension})'
        )
        value = ingredient.quantity
        if key in dict_:
            dict_[key] += value
        else:
            dict_[key] = value
    ingredients_list = ''
    for key, value in dict_.items():
        ingredients_list += f'{key} - {value}'
        ingredients_list += '\r\n'
    response = HttpResponse(
        ingredients_list,
        content_type='application/text charset=utf-8',
    )
    response['Content-Disposition'] = (
        'attachment; filename="ingredients_list.txt"'
    )
    print(ingredients_list)
    return response


class AboutAuthorView(TemplateView):
    template_name = 'static.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об авторе'
        context['image'] = 'author.jpg'
        context['author'] = {
            'name': 'Денис Докторов',
            'github_url': 'https://github.com/docker581/',
        }
        context['list_name'] = 'Интересы'
        context['list'] = [
            'Darkwave / synthpop',
            'Game theory',
            'Travels',
        ]
        return context


class AboutTechView(TemplateView):
    template_name = 'static.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Технологии'
        context['image'] = 'tech.jpg'
        context['list_name'] = 'Стек технологий'
        context['list'] = [
            'Python 3.8.5',
            'Django 3.0.5',
            'Django Rest Framework (DRF) 3.12.4',
        ]
        return context
