from django.shortcuts import render
from .models import Recipe

# Create your views here.


def index(request):

    context_dict = {'recipes': Recipe.objects.all()}

    return render(request, 'fooddance/index.html', context_dict)
