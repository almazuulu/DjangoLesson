from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    allNews = News.objects.all()
    context = {
        'allnews': allNews,
    }
    return render(request, 'newsapp/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id)
    category = Category.objects.get(pk = category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, 'newsapp/category.html', context = context)


def show_news(request,news_id):
    article = News.objects.get(id = news_id)
    context = {
        "article":article
    }
    return render(request, 'newsapp/article.html', context=context)



def about(request):
    return render(request, 'newsapp/aboutus.html')

def contact_us(request):
    return render(request, 'newsapp/contactus.html')

