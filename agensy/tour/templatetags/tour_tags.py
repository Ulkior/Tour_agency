from django import template

from ..models import *

register = template.Library()


@register.simple_tag()
def get_tours():
    return Tours.objects.all()