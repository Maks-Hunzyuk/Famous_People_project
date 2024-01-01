from django import template
from people.views import categories_db


register = template.Library()


@register.simple_tag()
def get_categories():
    return categories_db


@register.inclusion_tag('people/list_categories.html')
def show_categories(category_selected=0):
    categories = categories_db
    return {'categories': categories, 'category_selected': category_selected}