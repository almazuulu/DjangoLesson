from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView

class HomeNews(ListView):
    #object_list
    model = News
    template_name = 'newsapp/index.html'
    context_object_name = 'allnews'
    # region_list = ['Bishkek', 'Osh', 'JA', 'Talas', 'IK', 'Naryn', 'Batken']
    # extra_context = {'title': 'Новости Кыргызстана'}

    def get_context_data(self,*, object_list =None,  **kwargs):
        context = super().get_context_data(**kwargs)
        # region_list = ['Bishkek', 'Osh', 'JA', 'Talas', 'IK', 'Naryn', 'Batken']
        # context['regions'] = region_list
        context['title'] = 'И Новости Кыргызстана'

        return context

    def get_queryset(self):
        return News.objects.filter(is_published = True)

# def index(request):
#     allNews = News.objects.all()
#     context = {
#         'allnews': allNews,
#         'title': 'Главные новости'
#     }
#     return render(request, 'newsapp/index.html', context=context)

class NewsByCategory(ListView):
    model = News
    template_name = 'newsapp/category.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Новости Кыргызстана'}

    def get_context_data(self,*, object_list =None,  **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'],
                                   is_published = True)

# def get_category(request, category_id):
#     news = News.objects.filter(category_id = category_id)
#     category = Category.objects.get(pk = category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, 'newsapp/category.html', context = context)

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
            # print(form)
            news = form.save()
            return redirect('mainpage')
    else:
        form = NewsForm()
    return render(request, 'newsapp/add_news.html', {'form':form})

def about(request):
    return render(request, 'newsapp/aboutus.html')

def contact_us(request):
    return render(request, 'newsapp/contactus.html')

