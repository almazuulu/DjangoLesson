from django.contrib import admin
from django import forms
from .models import News, Category, Aboutus
from ckeditor.widgets import CKEditorWidget

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'created_at', 'updated_at', 'category', 'is_published')

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Aboutus)

# Register your models here.

