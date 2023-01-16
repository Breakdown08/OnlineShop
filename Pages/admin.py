from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from .models import *

admin.site.register(New)
admin.site.register(Product)
admin.site.register(ChildCategory)
admin.site.register(Category)