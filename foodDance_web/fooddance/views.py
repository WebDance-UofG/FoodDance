from django.shortcuts import render
from .models import Recipe, UserProfile, Comment, RecipeStep
from django.db.models import Avg
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def dict2obj(args):
    """
    transfer a dict to a obj
    """
    class obj(object):
        def __init__(self, d):
            for a, b in d.items():
                if isinstance(b, (list, tuple)):
                    setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
                else:
                    setattr(self, a, obj(b) if isinstance(b, dict) else b)
    return obj(args)


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
                "author": recipe.author,
                "slug": recipe.slug,
            })
        )
    recipes.sort(key=takeAverage)
    context_dict = {'recipes': recipes}
    return render(request, 'fooddance/category_allrecipes.html', context_dict)


def index(request, message=None):
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
                "author": recipe.author,
                "slug": recipe.slug,
            })
        )
    recipes.sort(key=takeAverage)
    recipes.reverse()
    context_dict = {'recipes': recipes[:9]}
    message = get_message_session_handler(request)
    if message:
        context_dict['alert_message'] = message
    return render(request, 'fooddance/index.html', context_dict)


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
                        "slug": recipe.slug,
                        "author_profile": UserProfile.objects.get(user_id=recipe.author.id),
                    })
                )
    context_dict = {'recipes': recipes}
    return render(request, 'fooddance/search.html',context_dict)


def detail(request, recipe_title_slug, message=None):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        recipe.views = recipe.views + 1
        recipe.save()
        context_dict['recipe'] = recipe
        context_dict['author_profile'] = UserProfile.objects.get(user_id=recipe.author.id)
        context_dict['avg'] = int(Comment.objects.filter(recipe__id=recipe.id).aggregate(Avg('rating'))['rating__avg'])
        context_dict['collect'] = UserProfile.objects.filter(collections__slug=recipe.slug).count()
        context_dict['steps'] = RecipeStep.objects.filter(recipe_id=recipe.id)
        context_dict['comments'] = Comment.objects.filter(recipe__id=recipe.id)
        context_dict['materials'] = Materials.objects.filter(recipe__id=recipe.id)

    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/index/')
        else:
            print(form.errors)

    context_dict['form'] = form
    if message:
        context_dict['alert_message'] = message

    return render(request, 'fooddance/detail.html', context=context_dict)


def user_register(request):
    context_dict = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        userTuple = User.objects.get_or_create(username=username)
        print(userTuple)
        if not userTuple[1]:
            context_dict['error'] = 'The user is already exist!'
        else:
            user = userTuple[0]
            user.set_password(password)
            user.email = email
            user.save()
            update_message_session_handler(request,'successfully register!')
            return redirect(reverse('fooddance:index'))

    return render(request, 'fooddance/register.html',context_dict)


def user_login(request):
    """
    login view
    """
    context_dict = {}

    if request.user.is_authenticated:
        update_message_session_handler(request, "You are logged in.")
        return redirect(reverse("fooddance:index"))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                update_message_session_handler(request, "successful login")
                login(request, user)
                return redirect(reverse('fooddance:index'))
            else:
                context_dict['login_error'] = "Your account is disabled."
        else:
            context_dict['login_error'] = "Check your username or password."

    return render(request, 'fooddance/login.html', context=context_dict)


# get message from server session
def get_message_session_handler(request):
    message = request.session.get('message')
    if message:
        del request.session['message']
        return message
    return None


# update message in server session
def update_message_session_handler(request, message):
    request.session['message'] = message
    print(f'- add message session {message}')

def myRecipes(request):
    if request.method == 'POST':
        pass
