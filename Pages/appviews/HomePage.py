from ..utils import *

def homepage(request):
    data = {}
    all_categories = []
    #news = New.objects.all().filter(is_private=False)
    main_categories = Category.objects.all()
    for item in main_categories:
        child_categories = []
        child_categories.append({'value': ChildCategory.objects.filter(parent_category_id=item.id), 'products_count': None})
        # for category in child_categories['value']:
        #     products_count = Product.objects.filter(category_id=category.id).count()

        all_categories.append({'key': item.title, 'slug': item.slug, 'value': child_categories, 'childs_count': 2})
    data.update({'all_categories': all_categories})
    print(data)
    return render(request, 'Pages/HomePage.html', context=data)


