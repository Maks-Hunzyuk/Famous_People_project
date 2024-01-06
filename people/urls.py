from django.urls import path, register_converter

from .views import IndexTemplateView, about, ShowPostView, AddPageView, contact, login, PeopleCategoryView, TagPostListView
from .converters import FoundDigitsYearConverter


app_name = 'people'


register_converter(FoundDigitsYearConverter, 'year4')

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>/', ShowPostView.as_view(), name='post'),
    path('addpage/', AddPageView.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<slug:category_slug>/', PeopleCategoryView.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', TagPostListView.as_view(), name='tag')
]
