import os
import re
import warnings
import importlib
import inspect

#from fooddance.db.models.query import QuerySet
from fooddance.models import Recipe,Materials,RecipeStep,UserProfile,Comment
from populate_fooddance import populate
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class B5_baseTemplateTest(TestCase):
    """
    Check if base template and the links exist,
    and if the base template works.
    """
    def get_template(self, path_to_template):
        """
        helper function
        """
        f = open(path_to_template, 'r')
        template_str = ""
        
        for line in f:
            template_str=f"{template_str}{line}"
        
        f.close()
        return template_str
    
    
    def test_b5_base_template_exists(self):
        """
        Check if the b5_base template exsists.
        """
        template_base_path = os.path.join(setting.TEMPLATE_DIR, 'fooddance', 'b5_base.html')
        self.assertTrue(os.path.exists(template__b5_base_path),f"{FAILURE_HEADER}Couln't find the b5_base.html{FAILURE_FOOTER}")
        
        
    def base_title_block(self):
        """
        Chcek if the b5_base template has the correct value.
        """
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'fooddance','b5_base.html')
        template_str=self.get_template(template_b5_base_path)
        
        title_pattern = r'(\s*|\n*)FoodDance(\s*|\n*)-(\s*|\n*){% block title_block %}(\s*|\n*){% (endblock|endblock title_block) %}(\s*|\n*)'
        self.assertTrue(re.search(title_pattern, template_str), f"{FAILURE_HEADER}Unexpected title block!{FAILURE_FOOTER}")
        
    
    def test_for_links_in_b5_base(self):
        template_str = self.get_template(os.join(setting.TEMPLATE_DIR,
                                         'fooddance', 'b5_base.html'))
        
        look_for=[
            #'<a href="{% url 'fooddance:index' %}"></a>',
            #'<a href="{% url 'fooddance:all_recipes' %}"></a>',
            '<a href="https://www.facebook.com">Facebook</a>',
            '<a href="https://www.facebook.com">Twitter</a>',
        ]
        
        for lookup in look_for:
            self.assertTrue(lookup in template_str, f"{FAILURE_HEADER}Missing '{lookup}' in b5_base.html!{FAILURE_FOOTER}")
    
        def test_template_usage(self):
        """
        Check that each view uses the correct template.
        """
        populate()
        
        urls = [reverse('FoodDance:detail'),]

        templates = [
                     'FoodDance/detail.html',]
        
        for url, template in zip(urls, templates):
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    


class SearchRecipeTest(TestCase):
    """
    Test if the search recipe has the right result.
    """
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('fooddance:search/?search=cake&searchbutton=search'))
        self.content = self.response.content.decode()
        
    
    def test_search_recipe_result(self):
        expected_recipe_title = "chocolate cake"
    
        self.assertTrue('recipe.title' in self.response.context, f"{FALURE_HEADER}The recipe.title variable couldn't be found in the context dictionary for the search() view.{FAILURE_FOOTER}")
        self.assertEqual(expected_recipe_title, self.response.context['recipe_title'], f"{FAILURE_HEADER}Wrong recipe title return{FAILURE_FOOTER}")
        self.assertTemplatedUsed(response, 'templates/search.html')
        
    
    def test_template_usage(self):
        """
        Check that each view uses the correct template.
        """
        populate()
        
        urls = [reverse('FoodDance:search'),]

        templates = ['FoodDance/search.html',]
        
        for url, template in zip(urls, templates):
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    def test_title_blocks(self):
        """
        Tests whether the title blocks in each page are the expected values.
        This is probably the easiest way to check for blocks.
        """
        populate()
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'FoodDance')
        
        mappings = {
            reverse('FoodDance:search'): {'full_title_pattern': r'<title>(\s*|\n*)FoodDance(\s*|\n*)-(\s*|\n*)search FoodDance(\s*|\n*)</title>',
                                     'block_title_pattern': r'{% block title_block %}(\s*|\n*)search FoodDance(\s*|\n*){% (endblock|endblock title_block) %}',
                                     'template_filename': 'search.html'},
        }

        for url in mappings.keys():
            full_title_pattern = mappings[url]['full_title_pattern']
            template_filename = mappings[url]['template_filename']
            block_title_pattern = mappings[url]['block_title_pattern']

            request = self.client.get(url)
            content = request.content.decode('utf-8')
            template_str = self.get_template(os.path.join(template_base_path, template_filename))

            self.assertTrue(re.search(full_title_pattern, content), f"{FAILURE_HEADER}Couldn't find the correct <title> block.{FAILURE_FOOTER}")
            self.assertTrue(re.search(block_title_pattern, template_str), f"{FAILURE_HEADER}Couldn't find the correct template block.{FAILURE_FOOTER}")
    
    
    def test_for_links_in_base(self):
        """
        There should be three hyperlinks in base.html, as per the specification of the book.
        Check for their presence, along with correct use of URL lookups.
        """
        template_str = self.get_template(os.path.join(settings.TEMPLATE_DIR, 'FoodDance', 'base.html'))

        look_for = [
            '<a href="{% url \'FoodDance:add_category\' %}">Add a New Category</a>',
            '<a href="{% url \'FoodDance:search\' %}">search</a>',
            '<a href="{% url \'FoodDance:index\' %}">Index</a>',
        ]
        
        for lookup in look_for:
            self.assertTrue(lookup in template_str, f"{FAILURE_HEADER}Couldn't find the hyperlink '{lookup}'.{FAILURE_FOOTER}")