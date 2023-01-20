from ..utils import *
from django.http import HttpResponse
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
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product_id = body['id']
        user = request.user
        existing_products_in_bag = BagProduct.objects.filter(user_id=user.id, product_id=product_id)
        if existing_products_in_bag.count() > 0:
            obj = existing_products_in_bag.first()
            obj.count += 1
            obj.save()
        else:
            BagProduct.objects.create(user_id=user.id, product_id=product_id, count=1).save()
        return HttpResponse("товар добавлен в корзину")

    data = {}
    all_categories = fill_categories()
    news = get_last_news()
    user = request.user
    bag_products = []
    if user != 'AnonymousUser':
        bag_products = BagProduct.objects.filter(user__username=user)
    data.update({'all_categories': all_categories, 'news': news, 'bag_count': bag_products.count()})
    return render(request, 'Pages/HomePage.html', context=data)


def category(request, slug):
    data = {}
    all_categories = fill_categories()
    products = get_products(slug)
    current_category = ChildCategory.objects.filter(slug__iexact=slug).first()
    user = request.user
    bag_products = []
    if user != 'AnonymousUser':
        bag_products = BagProduct.objects.filter(user__username=user)
    data.update({'all_categories': all_categories, 'products': products, 'category': current_category,
                 'bag_count': bag_products.count()})
    return render(request, 'Pages/Categories.html', context=data)
