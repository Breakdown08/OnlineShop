from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from math import ceil


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


def pack(object, size):
    count_pages = ceil(len(object) / size)
    objects_page = []
    results_array = []
    step = 0
    counter = 0
    for i in range(count_pages):
        for j in range(size):
            counter += 1
            if j + step == len(object):
                break
            item = object[j + step]
            item.update({'page': counter})
            objects_page.append(item)
        step += size
        results_array.append(objects_page)
        objects_page = []
    return results_array
