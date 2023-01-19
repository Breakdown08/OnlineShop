import os
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def path(self):
    if str(self).__contains__('media'):
        return str(self)
    else:
        return 'media/'+str(self)