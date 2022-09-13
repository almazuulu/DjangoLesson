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


