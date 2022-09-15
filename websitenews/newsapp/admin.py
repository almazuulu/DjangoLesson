from django.contrib import admin
from .models import News, Category, Aboutus

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category', 'is_published')

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Aboutus)

# Register your models here.

