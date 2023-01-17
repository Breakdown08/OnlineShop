from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db import models
from django.shortcuts import reverse


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=False)
    return new_slug


def transliterate(name):
    dictionary = {'а': 'a', 'б': 'b', 'в': 'w', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
                  'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                  'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
                  'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
                  'ю': 'u', 'я': 'ja', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
                  'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
                  'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
                  'Ц': 'C', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
                  'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
                  '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
                  ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
                  '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
                  'Є': 'e', '—': ''}
    for key in dictionary:
        name = name.replace(key, dictionary[key])
    return name


# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     # password1 = models.CharField(blank=True,max_length = 120,verbose_name='Новый пароль')
#     # password2 = models.CharField(blank=True,max_length = 120,verbose_name='Новый пароль (повторить)')
#
#     def get_absolute_url(self):
#         return reverse('profile_page', kwargs={'username': self.user.username})
#
#     def __str__(self):
#         return self.user.username


class New(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=20, verbose_name='Заголовок')
    short_description = models.TextField(verbose_name='Краткое описание новости', default=None, blank=True, null=False)
    image_original = models.ImageField(upload_to='news_images/', verbose_name='Главное изображение новости',
                                       default=None, null=True)
    link = models.CharField(max_length=512, verbose_name='Ссылка на товар', blank=True, default=None, null=True)
    created_at = models.DateField(default=timezone.now, verbose_name='Дата публикации')

    def __str__(self):
        return 'Новость: {}'.format(self.title)





class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=20, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, editable=True)

    def __str__(self):
        return 'Категория: {}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = transliterate(self.title)
        self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)


class ChildCategory(models.Model):
    class Meta:
        verbose_name = 'Вложенная категория'
        verbose_name_plural = 'Вложенные категории'

    title = models.CharField(max_length=20, verbose_name='Название')
    parent_category = models.ForeignKey(Category, related_name='parent_category', on_delete=models.SET_NULL, null=True,
                                        blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, editable=True)

    def __str__(self):
        return 'Вложенная категория: {}'.format(self.title) + ' ({})'.format(self.parent_category.title)

    def get_absolute_url(self):
        return reverse('category_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        self.slug = transliterate(self.title)
        self.slug = gen_slug(self.slug)
        self.slug = self.parent_category.slug + '-' + self.slug
        super().save(*args, **kwargs)


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    title = models.CharField(max_length=20, verbose_name='Заголовок')
    short_description = models.TextField(verbose_name='Краткое описание товара', default=None, blank=True, null=False)
    content = RichTextField(verbose_name='Полное описание товара')
    image_original = models.ImageField(upload_to='products_images/', verbose_name='Главное изображение товара',
                                       default=None, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True, verbose_name='Стоимость товара')
    category = models.ForeignKey(ChildCategory, related_name='this_category_products', on_delete=models.SET_NULL, null=True,
                                        blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, editable=True)

    def __str__(self):
        return 'Товар: {}'.format(self.title)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = transliterate(self.title)
        self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)