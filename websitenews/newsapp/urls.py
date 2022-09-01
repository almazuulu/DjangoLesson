from django.contrib import admin
from django.urls import path, re_path
from .views import index, about, contact_us, get_category
urlpatterns = [
    path('', index, name='mainpage'),
    path('category/<int:category_id>/', get_category),
    re_path(r'aboutus/', about, name='aboutus'),
    re_path(r'contactus/', contact_us, name = 'contactus')
]