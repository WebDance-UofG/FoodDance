from django.shortcuts import render
from .models import Recipe, UserProfile, Comment, RecipeStep
from django.db.models import Avg
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import datetime
import hashlib


# Create your views here.

def getAvg(recipe_id):
    avg = Comment.objects.filter(recipe__id=recipe_id).aggregate(Avg('rating'))['rating__avg']
    return int(avg) if avg else 0


def index(request):
    """
    The home page.
    """
    recipes = []
    for recipe in Recipe.objects.all():
        recipes.append(
            dict2obj({
                "title": recipe.title,
                "avg": getAvg(recipe.id),
                "image": recipe.image,
                "during": recipe.duration,
                "author": recipe.author,
                "slug": recipe.slug,
            })
        )

    def takeAverage(ele):
        return ele.avg
    # sort the list by avg
    recipes.sort(key=takeAverage)

    recipes.reverse()
    context_dict = {'recipes': recipes[:9]}

    wrapMessage(request, context_dict)

    return render(request, 'fooddance/index.html', context_dict)


def category_allrecipes(request):
    """
    A view show all recipes
    """
    recipes = []

    def takeAverage(ele):
        return ele.avg

    for recipe in Recipe.objects.all():
        recipes.append(
            dict2obj({
                "title": recipe.title,
                "avg": getAvg(recipe.id),
                "image": recipe.image,
                "during": recipe.duration,
                "author": recipe.author,
                "slug": recipe.slug,
            })
        )
    recipes.sort(key=takeAverage)
    context_dict = {'recipes': recipes}

    return render(request, 'fooddance/category_allrecipes.html', context_dict)


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
                        "avg": getAvg(recipe.id),
                        "image": recipe.image,
                        "author": recipe.author,
                        "overview": recipe.overview,
                        "comments": len(Comment.objects.filter(recipe__id=recipe.id)),
                        "likes": Comment.objects.filter(recipe__id=recipe.id).count(),
                        "views": recipe.views,
                        "slug": recipe.slug,
                        "author_profile": UserProfile.objects.get(user_id=recipe.author.id),
                    })
                )
    context_dict = {'recipes': recipes}
    return render(request, 'fooddance/search.html', context_dict)


def detail(request, recipe_title_slug):
    if request.method == 'POST':
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        rating = request.POST.get('ratingRadioOptions')
        content = request.POST.get('content')

        comment = Comment.objects.get_or_create(user=request.user, recipe=recipe)[0]

        if content:
            comment.content = content

        if rating:
            comment.rating = rating

        comment.save()
        return redirect(reverse('fooddance:detail', kwargs={'recipe_title_slug': recipe_title_slug}))

    context_dict = {}

    showComment = False
    showRating = False

    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        recipe.views = recipe.views + 1
        recipe.save()

        relating_comments = Comment.objects.filter(recipe__id=recipe.id)

        context_dict['recipe'] = recipe
        context_dict['likes'] = relating_comments.filter(like=True).count()
        context_dict['author_profile'] = UserProfile.objects.get(user_id=recipe.author.id)
        avg = relating_comments.aggregate(Avg('rating'))['rating__avg']
        context_dict['avg'] = avg if avg else 0
        context_dict['collect'] = UserProfile.objects.filter(collections__slug=recipe.slug).count()
        context_dict['steps'] = RecipeStep.objects.filter(recipe_id=recipe.id)
        context_dict['comments'] = relating_comments
        context_dict['materials'] = Materials.objects.filter(recipe__id=recipe.id)

        if request.user.is_authenticated:
            context_dict['hasCollect'] = UserProfile.objects.get(user=request.user). \
                                             collections.filter(slug=recipe_title_slug).count() > 0
            try:
                comment = Comment.objects.get(recipe=recipe, user=request.user)
                context_dict['hasLike'] = comment.like
            except Comment.DoesNotExist:
                context_dict['hasLike'] = False

            show_comment = True
            show_rating = True

            try:
                comment = Comment.objects.get(recipe__slug=recipe_title_slug, user__id=request.user.id)
            except Comment.DoesNotExist:
                comment = None

            if comment and len(comment.content) != 0:
                show_comment = False

            if comment and int(comment.rating) > 0:
                show_rating = False

            context_dict['showComment'] = show_comment
            context_dict['showRating'] = show_rating

    except Recipe.DoesNotExist:
        return HttpResponse('recipe does not exist')

    return render(request, 'fooddance/detail.html', context=context_dict)


def user_register(request):
    context_dict = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        username_check = False
        email_check = False

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            username_check = True
        finally:
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                email_check = True

        if not email_check and not username_check:
            context_dict['error'] = 'The email and username has already been used!'
        elif not email_check:
            context_dict['error'] = 'The email has already been used!'
        elif not username_check:
            context_dict['error'] = 'The username is already exist!'
        else:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.email = email
            user.is_staff = True
            user.is_superuser = True

            user.save()

            up = UserProfile.objects.get_or_create(user=user)[0]
            up.save()

            update_session_handler(request, 'successfully register, please check our email for confirmation!!!')

            code = make_confirm_string(user)
            send_confirmation_email(email, code)

            return redirect(reverse('fooddance:user_login'))

    return render(request, 'fooddance/register.html', context_dict)


def user_login(request):
    """
    login view
    """
    context_dict = {}

    if request.user.is_authenticated:
        update_session_handler(request, "You are logged in.")
        return redirect(reverse("fooddance:index"))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                try:
                    up = UserProfile.objects.get(user=user)
                    if not up.has_confirmed:
                        context_dict['login_error'] = "Your account has noe been confirmed. Check your email!"
                    else:
                        update_session_handler(request, "successful login")
                        login(request, user)
                        return redirect(reverse('fooddance:index'))
                except UserProfile.DoesNotExist:
                    pass

            else:
                context_dict['login_error'] = "Your account is disabled."
        else:
            context_dict['login_error'] = "Check your username or password."

    wrapMessage(request, context_dict)
    return render(request, 'fooddance/login.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    update_session_handler(request, 'successfully log out')
    return redirect(reverse('fooddance:index'))


def like(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        recipe_id = request.POST.get('recipe')

        comment = \
            Comment.objects.get_or_create(user=User.objects.get(id=user_id), recipe=Recipe.objects.get(id=recipe_id))[0]

        if comment and comment.like:
            comment.like = False
            response = JsonResponse({'result': 'dislike'})
        else:
            comment.like = True
            response = JsonResponse({'result': 'like'})
        comment.save()
        return response


def collect(request):
    if request.method == 'POST':
        user = int(request.POST.get('user'))
        recipe = int(request.POST.get('recipe'))

        up = UserProfile.objects.get(user_id=user)

        if up.collections.filter(id=recipe).count() == 0:
            up.collections.add(Recipe.objects.get(id=recipe))
            response = JsonResponse({'result': 'collect'})

        else:
            up.collections.remove(Recipe.objects.get(id=recipe))
            response = JsonResponse({'result': 'discollect'})

        up.save()

        return response


def share(request):
    if request.method == 'POST':
        recipe = int(request.POST.get('recipe'))

        try:
            recipe = Recipe.objects.get(id=recipe)
            recipe.shares = recipe.shares + 1
            recipe.save()
            response = JsonResponse({'result': 'success'})
        except Recipe.DoesNotExist:
            response = JsonResponse({'result': 'failed'})

        return response


def user_confirm(request):
    context_dict = {}
    code = request.GET.get('code', None)

    try:
        confirm = ConfirmString.objects.get(code=code)
    except ConfirmString.DoesNotExist:
        context_dict['message'] = 'Valid request'
        return render(request, 'fooddance/confirm.html', context_dict)

    c_time = confirm.creat_time
    now = datetime.datetime.now()
    expired_time = c_time + datetime.timedelta(settings.CONFIRM_DAYS)
    if now.date() > expired_time.date():
        confirm.user.delete()
        context_dict['message'] = 'Your confirmation is expired'
        return render(request, 'fooddance/confirm.html', context_dict)
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        context_dict['message'] = 'Thank you for your confirmation. You can login now.'
        return render(request, 'fooddance/confirm.html', context_dict)

def myrecipes(request):
    recipes = []

    def takeAverage(ele):
        return ele.avg

    if request.user.is_authenticated:
        for recipe in Recipe.objects.filter(author_id=request.user.id):
            recipes.append(
                dict2obj({
                    "title": recipe.title,
                    "avg": getAvg(recipe.id),
                    "image": recipe.image,
                    "author": recipe.author,
                    "overview": recipe.overview,
                    "comments": len(Comment.objects.filter(recipe__id=recipe.id)),
                    "likes": Comment.objects.filter(recipe__id=recipe.id).count(),
                    "views": recipe.views,
                    "slug": recipe.slug,
                })
            )
        context_dict = {'recipes': recipes}
    else:
        return render(request, 'fooddance/login.html')

    return render(request, 'fooddance/myrecipes.html', context_dict)


# some helper methods
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


def update_session_handler(request, message, cookie='message'):
    """
      update message in server session
    """
    request.session[cookie] = message
    print(f'- add message session {message}')


def get_session_handler(request, cookie='message'):
    """
       get message from server session
    """
    message = request.session.get(cookie)
    if message:
        del request.session[cookie]
        return message
    return None


def wrapMessage(request, context_dict):
    """
        wrap the message in session into context dict
    """
    message = get_session_handler(request)
    if message:
        context_dict['alert_message'] = message


def hash_code(s, salt='webdance'):
    """
    generate a hash code
    """
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def mycollection(request):
    # recipes = []
    # userid = request.user.id
    # userprofiles = UserProfile.objects.fileter(user_id=userid)
    #
    # print(type(userprofiles))
    # pass
    # def takeAverage(ele):
    #     return ele.avg
    pass

def make_confirm_string(user):
    """
        generate and store a confirm code
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.username, now)
    ConfirmString.objects.create(code=code, user=UserProfile.objects.get(user=user))
    return code


def send_confirmation_email(email, code):
    from django.core.mail import EmailMultiAlternatives

    subject = 'Email confirmation'

    text_content = '''If you see this, it means your email does not support html. Please contact the administrator.'''

    html_content = ''' <h3>Welcome!</h3>
                      <p>We're excited to have you get started. First, you need to confirm your account. Just click the link below. </p>
                      <a href="{}/confirm/?code={}" target=blank>{}</a>
                      '''.format(settings.WEB_URL, code, settings.WEB_URL,settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
