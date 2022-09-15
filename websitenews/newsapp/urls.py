from django.contrib import admin
from django.urls import path, re_path
from .views import *
urlpatterns = [
    # path('', index, name='mainpage'),
    path('', HomeNews.as_view(), name='mainpage'),
    # path('category/<int:category_id>/', get_category),
    path('category/<int:category_id>/', NewsByCategory.as_view(
        extra_context = {
            'title': 'Новость категория',
        }), name = 'category'),
    # path('article/<int:news_id>/',show_news, name='show_news'),
    path('article/<int:news_id>/',DetailNews.as_view(), name='show_news'),
    path('article/add-news/', CreateNews.as_view(), name = 'add_news'),
    # path('article/add-news/', add_news, name='add_news'),
    path('successemail', successemail, name = 'successemail'),
    re_path(r'aboutus/', about, name='aboutus'),
    re_path(r'contactus/', contact_us, name = 'contactus'),

]