import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineShop.settings')
django.setup()
from Pages.models import Category, ChildCategory, Product


def get_or_create(model, **kwargs):
    objects = model.objects.filter(title=kwargs['title'])
    if objects.count() > 0:
        result = objects.first()
        return result
    else:
        result = model.objects.create(**kwargs)
        return result


main_category1 = get_or_create(Category, title="Овощи")
main_category2 = get_or_create(Category, title="Прочее")
main_category1.save()
main_category2.save()
child_category1 = get_or_create(ChildCategory, title="Перцы", parent_category=main_category1)
child_category2 = get_or_create(ChildCategory, title="Мед", parent_category=main_category2)

child_category1.save()
child_category2.save()

Product.objects.create(title="Колода 36 карт", category=child_category1, content="Классическая колод а карт 36 штук",
                       price=100, short_description='карты 36 штук', image_original="media/organic-food/p4.jpg").save()
Product.objects.create(title="Колода 54 карты", category=child_category1,
                       content='Карты для игры "Покер" или "Блэкджек"', price=150, short_description='карты 54 штуки',
                       image_original="media/organic-food/p4.jpg").save()
Product.objects.create(title="Фишки для покера 100 штук", category=child_category2,
                       content='Фишки для игры "Покер" или "Блэкджек"', price=200,
                       short_description="Маленький набор фишек", image_original="media/organic-food/p4.jpg").save()
Product.objects.create(title="Фишки для покера 500 штук", category=child_category2,
                       content='Фишки для игры "Покер" или "Блэкджек"', price=500,
                       short_description="Большой набор фишек", image_original="media/organic-food/p4.jpg").save()
