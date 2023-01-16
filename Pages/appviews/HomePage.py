from ..utils import *
from pprint import pprint

def fill_categories():
    all_categories = []
    main_categories = Category.objects.all()
    for main_category in main_categories:
        child_categories = ChildCategory.objects.filter(parent_category_id=main_category.id)
        all_categories.append({'key': main_category.title, 'slug': main_category.slug, 'child_categories': child_categories, 'count': child_categories.count()})
    return all_categories


def get_last_news():
    news = New.objects.all()[:3]

def homepage(request):
    data = {}
    all_categories = fill_categories()
    news = get_last_news()
    data.update({'all_categories': all_categories, 'news': news})
    pprint(data)
    return render(request, 'Pages/HomePage.html', context=data)


