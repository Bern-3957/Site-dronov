from django import template
from bboard.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Rubric.objects.all()