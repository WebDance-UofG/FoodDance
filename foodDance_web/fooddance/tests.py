from django.test import TestCase
from population_script import populate, recipes, users, collections
from fooddance.models import *
from django.test import Client
from django.template.defaultfilters import slugify


# Create your tests here.


class viewTestCase(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        # populate the test data
        populate(mode="test")
        self.client = Client()

    def test_index_view_response(self):
        response = self.client.get("")
        # check if it works
        self.assertEqual(response.status_code, 200,
                         f"Get home page failed. Check the index view.")

        # is header loaded
        recommendation_titles = ["Volcanic Lava Egg", "Oatmeal and Avocado Tart",
                                 "Beef Donburi", "Poke Bowl", "Avocado and Shrimp Sandwich with Egg Cream", "Americano",
                                 "Sauteed Cauliflower with Mushrooms", "Chicken Casserole", "Red Bean Jicama"]

        content = response.content.decode()

        for title in recommendation_titles:
            self.assertIn(
                '''<p class=\"text-center recom-recipe-title\">{}</p>'''.format(title), content,
                          '''Recipe {} should be in the home page. Please check.'''.format(title))

    def test_allrecipes_view_response(self):
        response = self.client.get("/allrecipes/")
        self.assertEqual(response.status_code, 200,
                         f"Get category_allrecipes page failed. Check the index view.")

        content = response.content.decode()

        for recipe in recipes:
            # detect title
            self.assertIn(
                ''' <p class="text-center recipe-title">{}</p>'''.format(recipe['title']), content,
                          '''Recipe title {} should be in the recipes list. Please check.'''.format(recipe['title']))
            # detect duration
            self.assertIn(
                ''' <p class="recipe-text">{} min</p>'''.format(recipe['duration']), content,
                          '''Recipe durattion {} - {} should be in the recipes list. Please check.'''.format(recipe['duration'],recipe['title']))
            # detect author
            self.assertIn(
                ''' <p class="recipe-text">{}</p>'''.format(recipe['author']), content,
                          '''Recipe author {} - {} should be in the recipes list. Please check.'''.format(recipe['author'],recipe['title']))

    def test_search_view_response(self):

        test_keywords = [
            {"key": "chicken",
                "results": ["Chicken Casserole", "Roast chicken"]
            },
            {"key": "egg",
                "results": ["Volcanic Lava Egg", "Low Fat North African Egg",
                     "Avocado and Shrimp Sandwich with Egg Cream"]
             },
        ]

        for keyword in test_keywords:
            response = self.client.get("/search/?search={}".format(keyword["key"]))

            self.assertEqual(response.status_code, 200,
                             "Search {} failed.".format(keyword["key"]))

            content = response.content.decode()
            for result in keyword['results']:
                self.assertIn(
                    '''<p class="row search-detail-title">{}</p>'''.format(result), content,
                    '''Result {}  should be in the {} search results. Please check.'''.format(result, keyword['key']))

    def test_detail_view_response(self):
        for recipe in recipes:
            response = self.client.get("/detail/{}/".format(slugify(recipe['title'])))

            self.assertEqual(response.status_code, 200,
                             "Open {} detial page failed.".format(recipe['title']))

            content = response.content.decode()

            # detect title
            self.assertIn(
                '''<h3>{}</h3>'''.format(recipe['title']), content,
                '''Title {}  should be in the {} detail p[age. Please check.'''.format(recipe['title'], recipe['title']))

            # detect author
            self.assertIn(
                '''<p id="userName">{}</p>'''.format(recipe['author']), content,
                '''Author {}  should be in the {} detail p[age. Please check.'''.format(recipe['author'], recipe['title']))

            # detect duration
            self.assertIn(
                '''<p class="clearBottomMargin">{} mins</p>'''.format(recipe['duration']), content,
                '''Duration {}  should be in the {} detail p[age. Please check.'''.format(recipe['duration'], recipe['title']))

            # detect Difficulty
            difficulty = ('Difficult' if recipe['difficulty'] >= 4 else
                         ('Medium' if recipe['difficulty'] > 3 else 'Easy'))

            self.assertIn(
                '''<p class="clearBottomMargin">{}</p>'''.format(difficulty), content,
                '''Difficulty {}  should be in the {} detail p[age. Please check.'''.format(difficulty, recipe['title']))

            # detect materials
            for material in recipe['materials']:
                self.assertIn('''<p>{}</p>'''.format(material['ingredient']), content,
                                                     '''Material {} should be in the {} detail p[age. Please check.'''.format(material['ingredient'],recipe['title']))


