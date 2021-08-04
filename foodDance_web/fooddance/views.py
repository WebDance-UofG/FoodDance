from django.shortcuts import render
from .models import Recipe

# Create your views here.


def index(request):

    context_dict = {'recipes': Recipe.objects.all()}

    return render(request, 'fooddance/index.html', context_dict)


def detail(request, recipe_title_slug):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        context_dict['recipe'] = recipe
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'fooddance/detail.html', context=context_dict)
