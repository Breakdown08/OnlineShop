import os
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def path(self):
    print(str(self))
    return str(self)