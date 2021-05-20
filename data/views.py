from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import User, Recipe, Tag, RecipeIngredient
from .forms import RecipeForm


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
