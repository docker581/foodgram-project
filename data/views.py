from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Recipe, Tag


def index(request):
    latest = Recipe.objects.all()[:6]
    tags = Tag.objects.all()
    return render(request, 'index.html', {'recipes': latest, 'tags': tags})