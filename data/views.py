from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(
        request, 
        'index.html', 
    )