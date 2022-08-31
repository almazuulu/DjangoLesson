from django.contrib import admin
from django.urls import path, re_path
from .views import index, about, contact_us
urlpatterns = [
    path('', index, name='mainpage'),
    re_path(r'aboutus/', about, name='aboutus'),
    re_path(r'contactus/', contact_us, name = 'contactus')
]