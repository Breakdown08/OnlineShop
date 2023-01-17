from django.urls import include, re_path
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
# from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/logout/', homepage, name='post-logout'),
    path('', homepage, name='homepage_url'),
    path('contacts', contacts, name='contacts_url'),
    path('about', about, name='about_url'),
    path('delivery', delivery, name='delivery_url'),
    path('<str:slug>/', category, name='category_url'),
    # path('news/<str:slug>/', NewDetail.as_view(), name='new_detail_url'),
    # path('news/<str:slug>/edit/', UpdateNewView.as_view(), name='edit_url'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]