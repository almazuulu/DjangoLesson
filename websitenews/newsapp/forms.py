from django import forms
from .models import Category, News
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Имя пользователя должно состоят из более 5 букв',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', help_text='Пароль должен состоять из более 8 букв',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label = 'Имя пользователя', help_text = 'Имя пользователя должно состоят из более 5 букв',
        widget = forms.TextInput(attrs = {'class': 'form-control'}))
    password1 = forms.CharField(label = 'Пароль', help_text = 'Пароль должен состоять из более 8 букв',
        widget = forms.PasswordInput(attrs = {'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', help_text = 'Пароль должен совпадать с предыдущим паролем',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label = 'Email',
        widget = forms.EmailInput( attrs = {'class': 'form-control'} ))

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','content','photo','is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs = {"class":"form-control mb-3"}),
            'content': CKEditorWidget(),
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

    captcha = CaptchaField()





