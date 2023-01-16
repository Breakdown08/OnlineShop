from ..utils import *
from pprint import pprint

def fill_categories():
    all_categories = []
    main_categories = Category.objects.all()
    for main_category in main_categories:
        child_categories = []
        items = ChildCategory.objects.filter(parent_category_id=main_category.id)
        child_categories.append({'items': items, 'count': items.count()})
        all_categories.append({'key': main_category.title, 'slug': main_category.slug, 'child_categories': child_categories, 'count': len(child_categories)})
    return all_categories

def homepage(request):
    data = {}
    all_categories = fill_categories()
    data.update({'all_categories': all_categories})
    pprint(data)
    return render(request, 'Pages/HomePage.html', context=data)


