'''
Création : 2018-03-22

@author: Eric Lapouyade
'''
from django import template
from django.utils.safestring import mark_safe
from django_robohash.robotmaker import make_robot_svg
register = template.Library()


@register.simple_tag()
def robohash(string, width=300, height=300, *args, **kwargs):
    return mark_safe(make_robot_svg(string, width, height))