from django import template
from newsapp.models import Category

register = template.Library()

@register.simple_tag()
def get_categories(name='get_list_categories'):
    return Category.objects.all()

@register.inclusion_tag('newsapp/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}