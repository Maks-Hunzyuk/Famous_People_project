from django.urls import path, register_converter

from people.views import index, about, show_post, add_page, contact, login, show_category
from people.converters import FoundDigitsYearConverter


app_name = 'people'


register_converter(FoundDigitsYearConverter, 'year4')

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('addpage/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:category_id>/', show_category, name='category')
]
