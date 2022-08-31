from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category', 'is_published')

admin.site.register(News, NewsAdmin)
admin.site.register(Category)

# Register your models here.

