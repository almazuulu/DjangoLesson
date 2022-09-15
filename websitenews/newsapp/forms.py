from django import forms
from .models import Category, News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','content','photo','is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs = {"class":"form-control mb-3"}),
            'content': forms.Textarea(attrs = {"class":"form-control mb-3"}),
            'category':forms.Select(attrs = {"class": "form-select mt-3"}),
        }

class ContactForm(forms.Form):
    # name = forms.CharField(max_length=200, required = True, label = 'Ваше имя',
    #                        widget = forms.TextInput(attrs = {"class": "input1", "placeholder": "Введите свое имя"}))
    email = forms.EmailField(required=True, label='Ваш почтовый адрес',
                           widget=forms.EmailInput(attrs={"class": "input1", "placeholder": "Введите свой email"}))
    subject = forms.CharField(max_length=300, required = True, label = "Тема сообщения", widget = forms.TextInput(
        attrs = {"class": "input1", "placeholder": "Введите тему сообщения"}))
    message = forms.CharField(required = True, label = 'Сообщение', widget = forms.Textarea(
        attrs = {"class": "input1", "placeholder": "Введите свое сообщение"}
    ))

    # title = forms.CharField(max_length=250, label= 'Заголовок новости', widget = forms.TextInput(
    #     attrs = {"class":"form-control"}
    # ))
    # content = forms.CharField(label = 'Содержание новости', widget = forms.Textarea(
    #     attrs = {"class":"form-control",
    #              "rows":10}
    # ))
    # is_published = forms.BooleanField(label = 'Опубликовано?', initial = True)
    # category = forms.ModelChoiceField(empty_label = 'Выберите категорию',
    #                                   queryset=Category.objects.all(), label = 'Категория',
    #                                   widget = forms.Select(
    #                                 attrs = {"class": "form-select"}))
    # #photo


