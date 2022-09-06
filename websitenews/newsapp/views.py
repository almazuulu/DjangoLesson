from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm

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

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            # title = form.cleaned_data['title']
            # News.objects.create(title = title)
            news = News.objects.create(**form.cleaned_data)
            return redirect('mainpage')
    else:
        form = NewsForm()
    return render(request, 'newsapp/add_news.html', {'form':form})

def about(request):
    return render(request, 'newsapp/aboutus.html')

def contact_us(request):
    return render(request, 'newsapp/contactus.html')

