from ..utils import *
from pprint import pprint


def fill_categories():
    all_categories = []
    main_categories = Category.objects.all()
    for main_category in main_categories:
        child_categories = ChildCategory.objects.filter(parent_category_id=main_category.id)
        all_categories.append(
            {'key': main_category.title, 'slug': main_category.slug, 'child_categories': child_categories,
             'count': child_categories.count()})
    return all_categories


def get_last_news():
    news = New.objects.all()
    return news


def get_products(category_slug):
    products = Product.objects.filter(category__slug__iexact=category_slug)
    return products


def homepage(request):
    data = {}
    all_categories = fill_categories()
    news = get_last_news()
    data.update({'all_categories': all_categories, 'news': news})
    return render(request, 'Pages/HomePage.html', context=data)


def category(request, slug):
    data = {}
    all_categories = fill_categories()
    products = get_products(slug)
    current_category = ChildCategory.objects.filter(slug__iexact=slug).first()
    data.update({'all_categories': all_categories, 'products': products, 'category': current_category})
    return render(request, 'Pages/Categories.html', context=data)
