from django.shortcuts import render
from .models import Recipe, Comment
from django.db.models import Avg

# Create your views here.


def index(request):
    recipes = []

    def takeAverage(ele):
        return ele.avg

    for recipe in Recipe.objects.all():
        recipes.append(
            dict2obj({
                "title": recipe.title,
                "avg": "{:.1f}".format(Comment.objects.filter(recipe__id=recipe.id).aggregate(Avg('rating'))['rating__avg']),
                "image": recipe.image,
                "during": recipe.duration,
                "author": recipe.author
            })
        )
    recipes.sort(key=takeAverage)
    context_dict = {'recipes': recipes[:12]}
    return render(request, 'fooddance/index.html', context_dict)


def detail(request, recipe_title_slug):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        context_dict['recipe'] = recipe
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'fooddance/detail.html', context=context_dict)

def category_allrecipes(request):
    recipes = []

    def takeAverage(ele):
        return ele.avg

    for recipe in Recipe.objects.all():
        recipes.append(
            dict2obj({
                "title": recipe.title,
                "avg": "{:.1f}".format(
                    Comment.objects.filter(recipe__id=recipe.id).aggregate(Avg('rating'))['rating__avg']),
                "image": recipe.image,
                "during": recipe.duration,
                "author": recipe.author
            })
        )
    recipes.sort(key=takeAverage)
    context_dict = {'recipes': recipes}
    return render(request, 'fooddance/category_allrecipes.html', context_dict)

def dict2obj(args):
    class obj(object):
        def __init__(self, d):
            for a, b in d.items():
                if isinstance(b, (list, tuple)):
                    setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
                else:
                    setattr(self, a, obj(b) if isinstance(b, dict) else b)
    return obj(args)

def search(request):
    recipes = []

    def takeAverage(ele):
        return ele.avg

    if request.method == 'GET' and request.GET:
        keyword = request.GET.get("search").lower()
        # keywordlist = recivedKey.title.split(" ")
        for recipe in Recipe.objects.all():
            titleList = recipe.title.lower().split(" ")
            # titleList = titleLower.split(" ")
            if keyword in titleList:
                recipes.append(
                    dict2obj({
                        "title": recipe.title,
                        "avg": "{:.1f}".format(
                            Comment.objects.filter(recipe__id=recipe.id).aggregate(Avg('rating'))['rating__avg']),
                        "image": recipe.image,
                        "author": recipe.author,
                        "overview": recipe.overview,
                        "comments": len(Comment.objects.filter(recipe__id=recipe.id)),
                        "likes": recipe.likes,
                        "views": recipe.views,
                    })
                )
    context_dict = {'recipes': recipes}
    return render(request, 'fooddance/search.html',context_dict)
