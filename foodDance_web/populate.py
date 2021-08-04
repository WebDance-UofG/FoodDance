import os
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodDance_web.settings')

import django

django.setup()
from fooddance.models import *;


def populate():
    users = [
        {'username': 'test1', 'password': 'test123', 'email': 'test1@test.com'},
        {'username': 'test2', 'password': 'test123', 'email': 'test2@test.com'},
        {'username': 'test3', 'password': 'test123', 'email': 'test3@test.com'}
    ]

    recipes = [
        {'title': 'Vegan Cheesecake',
         'author': 'test1',
         'overview':
            "This no-bake vegan cheesecake, with its boozy Black Forest cherry topping, is a luxurious twist on a "
            "retro classic. It's completely delicious and just the thing for celebrations and parties. See the recipe "
            "tips for alternative topping ideas.For this recipe you will need a food processor or blender.",
         'duration': 30,
         'budget': 10,
         'difficulty': 5,
         'materials': [
             {'ingredient': 'vegan bourbon biscuits', 'weight': '200g'},
             {'ingredient': 'dairy-free margarine', 'weight': '75g'},
             {'ingredient': 'vegan dark chocolate', 'weight': '350g'},
             {'ingredient': 'cocoa butter', 'weight': '50g'},
             {'ingredient': 'extra-firm silken tofu', 'weight': '400g'},
         ],
         'steps': [
             {'content': 'Grease a deep 20cm/8in round springform cake tin and line the base and sides with baking paper.'},
             {'content': 'Mix the crushed biscuits with the melted margarine and 2 pinches of salt, spread evenly over the base of the prepared tin and press down firmly. Place in the fridge for 40 minutes.'},
             {'content': 'Melt the chocolate and cocoa butter (or coconut oil) in a heatproof bowl over a pan of gently simmering water, stirring occasionally, until smooth.'},
             {'content': 'Put the tofu, vanilla, sugar and oat crème fraiche into a blender or food processor and blend until smooth. Add the melted chocolate mixture and blend again, then add a pinch of salt. Spread over the chilled base and smooth the top. Place in the fridge for at least 4 hours or, better still, overnight.'},
             {'content': 'You can make the cherry compôte in advance, but keep it separate until serving. Put the cherries into a saucepan, add the cornflour and stir until all are coated. Pour in 2 tablespoons of the kirsch, the sugar and 100ml/3½fl oz water. Stir over a medium heat for 5–6 minutes, simmering gently until the sauce has thickened and the cherries are soft. Remove from the heat and stir in the remaining tablespoon of kirsch, adding lemon juice to taste. Cool, then place in the fridge if making ahead.'},
             {'content': 'To serve, carefully remove the cheesecake from the tin, peel away the lining paper and put the cheesecake on a serving plate. Spoon the boozy cherry compôte (warm, or stirred to loosen if chilled) over the cheesecake, letting the syrup and fruit run down the sides'},
         ],
         'comments': [
             {'user': 'test2', 'rating': 3, 'content': "I’d really like some ca-me:"},
             {'user': 'test3', 'rating': 2, 'content': "This cake is absolutely perfect it's so soft and delicious wow just wow"},
             {'user': 'test2', 'rating': 5, 'content': "i could really go for some cake me asf:"},
         ]
         },
    ]

    collections = [
        {
            'user': 'test2', 'recipe': 'Vegan Cheesecake',
        },
        {
            'user': 'test3', 'recipe': 'Vegan Cheesecake',
        },
    ]

    for user in users:
        user = add_user(user['username'], user['password'], user['email'])
        print(f'- {user}')

    for recipe in recipes:
        add_recipe(recipe['title'], recipe['author'], recipe['overview'], recipe['duration'],
                   recipe['budget'], recipe['difficulty'], recipe['materials'], recipe['steps'], recipe['comments'])

    for collection in collections:
        u = add_collection(collection['user'], collection['recipe'])
        print(f"- {collection['user']} collect {collection['recipe']}")


def add_user(username,password,email):
    user = User.objects.get_or_create(username=username, password=password, email=email)[0]
    user.save()
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    userprofile.save()
    return user


def add_recipe(title, author_name, overview, duration, budget, difficulty, materials, steps, comments):
    author = User.objects.get(username=author_name)
    r = Recipe.objects.get_or_create(title=title, author=author, overview = overview, duration = duration, budget = budget, difficulty = difficulty)[0]
    r.save()

    print(f'- {r}')

    for material in materials:
        m = add_material(r, material['ingredient'], material['weight'])
        print(f'- {m}')

    for step in steps:
        s = add_step(r, step['content'])
        print(f'- {s}')

    for comment in comments:
        c = add_comment(comment['user'], r, comment['rating'], comment['content'])
        print(f'- {c}')

    return r


def add_material(recipe, ingredient, weight):
    m = Materials.objects.get_or_create(recipe=recipe, ingredient=ingredient, weight=weight)[0]
    m.save()
    return m


def add_step(recipe, content):
    s = RecipeStep.objects.get_or_create(recipe=recipe, content=content)[0]
    time.sleep(0.5)
    return s


def add_comment(user_name, recipe, rating, content):
    u = User.objects.get(username=user_name)
    c = Comment.objects.get_or_create(recipe=recipe, user=u, rating=rating, content=content)[0]
    c.save()
    return c


def add_collection(user_name, recipe_title):
    u = UserProfile.objects.get(user__username=user_name)
    r = Recipe.objects.get(title=recipe_title)
    u.collections.add(r)
    return u


if __name__ == '__main__':
    print('Starting fooddance population script...')
    populate()