from django import forms
from .models import Category, News

class NewsForm(forms.Form):
    title = forms.CharField(max_length=250, label= 'Заголовок новости', widget = forms.TextInput(
        attrs = {"class":"form-control"}
    ))
    content = forms.CharField(label = 'Содержание новости', widget = forms.Textarea(
        attrs = {"class":"form-control",
                 "rows":10}
    ))
    is_published = forms.BooleanField(label = 'Опубликовано?', initial = True)
    category = forms.ModelChoiceField(empty_label = 'Выберите категорию',
                                      queryset=Category.objects.all(), label = 'Категория',
                                      widget = forms.Select(
                                    attrs = {"class": "form-select"}))
    #photo


