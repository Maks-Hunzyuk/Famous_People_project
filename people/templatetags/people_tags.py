from django import template

from people.models import Categories


register = template.Library()


@register.inclusion_tag('people/list_categories.html')
def show_categories(category_selected=0):
    categories = Categories.objects.all()
    return {'categories': categories, 'category_selected': category_selected}