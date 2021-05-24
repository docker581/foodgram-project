from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import User, Recipe, Tag, RecipeIngredient, Subscription
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
    recipes = Recipe.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(recipes, 5) 
    page_number = request.GET.get('page') 
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {
            'tags': tags,
            'page': page,
            'paginator': paginator,           
        }
    ) 


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('index')
    return render(
        request, 
        'new.html', 
        {
            'form': form, 
        }
    )


@login_required
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


@login_required
def profile(request, username):
    author = get_object_or_404(User, username=username)  
    recipes = Recipe.objects.filter(author=author)
    tags = Tag.objects.all()
    paginator = Paginator(recipes, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)    
    return render(
        request, 
        'profile.html', 
        {
            'author': author,
            'tags': tags,
            'page': page,
            'paginator': paginator,
        }
    )


@login_required
def favorites(request):
    favorites = Recipe.objects.filter(favorites__user=request.user)
    tags = Tag.objects.all()
    paginator = Paginator(favorites, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request, 
        'favorites.html', 
        {
            'favorites': favorites,
            'tags': tags,
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


class AboutAuthorView(TemplateView):
    template_name = 'static.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Об авторе'
        context['image'] = 'author.jpg'
        context['author'] = {
            'name': 'Денис Докторов',
            'github_url' : 'https://github.com/docker581/'
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