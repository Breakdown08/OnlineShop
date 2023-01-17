from django.urls import include, re_path
# from django.contrib.auth import views
from django.urls import path
from .views import *
# from django.contrib.auth import views as auth_views
# from django.urls import include
# from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # path('register/', register, name='register'),
    # path('accounts/', include("django.contrib.auth.urls")),
    # path('accounts/logout/', homepage, name='post-logout'),
    path('', homepage, name='homepage_url'),
    path('<str:slug>/', category, name='category_url'),
    # path('private/', private, name='private_news_url'),
    # path('about/', about, name='aboutpage_url'),
    # path('news/<str:slug>/', NewDetail.as_view(), name='new_detail_url'),
    # path('news/<str:slug>/edit/', UpdateNewView.as_view(), name='edit_url'),
    # path('create/', CreateNewView.as_view(), name='create_new_url'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]