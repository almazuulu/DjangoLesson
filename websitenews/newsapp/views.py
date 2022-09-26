from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Category, Aboutus
from .forms import NewsForm, ContactForm, UserRegistrationForm, UserLoginForm
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegistrationForm()

    return render(request, 'newsapp/register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mainpage')
    else:
        form = UserLoginForm()
    return render(request, 'newsapp/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')

def test(request):
    object = ['john', 'paul', 'george', 'ringo',
              'john1', 'paul1', 'george1', 'ringo1',
              'john2', 'paul2', 'george2', 'ringo2',
              'john3', 'paul3', 'george3', 'ringo3']

    paginator = Paginator(object, 2)
    page_num = request.GET.get('page', 1)
    page_object = paginator.get_page(page_num)

    return render(request, 'newsapp/test.html', {'page_obj': page_object})

class HomeNews(ListView):
    model = News
    template_name = 'newsapp/index.html'
    context_object_name = 'allnews'
    paginate_by = 3


    def get_context_data(self,*, object_list =None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости Кыргызстана'

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
        category_name = Category.objects.get(pk = self.kwargs['category_id'])
        context['title'] = category_name
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

class DetailNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template_name = 'newsapp/article.html'
    context_object_name = 'article'

# def show_news(request,news_id):
#     article = News.objects.get(id = news_id)
#     context = {
#         "article":article
#     }
#     return render(request, 'newsapp/article.html', context=context)

class CreateNews(CreateView):
    # model = News
    form_class  = NewsForm
    template_name = 'newsapp/add_news.html'

    def get_context_data(self,*, object_list =None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление новости'
        return context

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST,request.FILES)
#         if form.is_valid():
#             news = form.save()
#             return redirect('mainpage')
#     else:
#         form = NewsForm()
#     return render(request, 'newsapp/add_news.html', {'form':form})

def about(request):
    aboutus = Aboutus.objects.all()
    context = {
        "aboutus":aboutus,
        'title': 'О Нас'
    }
    return render(request, 'newsapp/aboutus.html', context = context)

def successemail(request):
    return render(request, 'newsapp/successemail.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email_visitor = form.cleaned_data['email']
            subject_visitor = form.cleaned_data['subject']
            content_message = form.cleaned_data['message']
            try:
                mail = send_mail(subject_visitor, content_message,
                                 email_visitor, ['almazovi4.a@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Error sending')

            return redirect('successemail')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'title': 'Обратная связь'
    }

    return render(request, 'newsapp/contactus.html', context = context)

