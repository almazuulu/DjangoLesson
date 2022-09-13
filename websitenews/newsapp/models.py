from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
# id - uuid
# title - varchar
# content - Text
# created_at - DateTime (дата создание новости)
# updated_at - DateTime(дата редактирование новости)
# photo - Image
#is_published - Boolean (True/ False) Опубликовано ли новость

class News(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250, verbose_name = 'Заголовок новости')
    content = models.TextField(blank=True, verbose_name = 'Содержание новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Время редактирования')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null = True, blank = True, verbose_name = 'Фото')
    is_published = models.BooleanField(default=True, verbose_name = 'Опубликовано')
    category = models.ForeignKey('Category', on_delete = models.PROTECT,
                                 null = True, verbose_name = 'Категория')

    def get_absolute_url(self):
        return reverse('mainpage', kwargs = {"pk": self.pk})

        # return reverse('show_news', kwargs={"pk": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Category(models.Model):
    title_category = models.CharField(max_length = 250, db_index = True,
                                      verbose_name = 'Имя категории')

    def __str__(self):
        return self.title_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title_category']