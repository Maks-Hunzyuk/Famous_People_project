from django.urls import path, register_converter

from people.views import index, categories, categories_by_slug, archive
from people.converters import FoundDigitsYearConverter


app_name = 'people'


register_converter(FoundDigitsYearConverter, 'years4')

urlpatterns = [
    path('', index, name='index'),
    path('categories/<int:category_id>/', categories, name='category'),
    path('categories/<slug:category_slug>/', categories_by_slug, name='category_by_slug'),
    path("^archive/<year4: year>/", archive, name='archive')
]
