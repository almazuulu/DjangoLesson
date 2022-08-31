from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    allNews = News.objects.all()
    allCategories = Category.objects.all()
    context = {
        'allnews': allNews,
        'categories': allCategories
    }
    return render(request, 'newsapp/index.html', context=context)

def about(request):
    return render(request, 'newsapp/aboutus.html')

def contact_us(request):
    return render(request, 'newsapp/contactus.html')

