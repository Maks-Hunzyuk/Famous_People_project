from django import template
from django.db.models import Count

from people.models import Categories, TagPost

register = template.Library()


@register.inclusion_tag('people/list_categories.html')
def show_categories(category_selected=0):
    categories = Categories.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'categories': categories, 'category_selected': category_selected}


@register.inclusion_tag('people/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}
