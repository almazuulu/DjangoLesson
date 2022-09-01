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

def get_category(request, category_id):
    # category = Category.objects.get(pk = category_id)
    news = News.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category

    }

    return render(request, 'newsapp/category.html', context = context)





def about(request):
    return render(request, 'newsapp/aboutus.html')

def contact_us(request):
    return render(request, 'newsapp/contactus.html')

