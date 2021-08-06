from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag(name='setting_tag')
def tag_func_name(name):
    return getattr(settings, name)
