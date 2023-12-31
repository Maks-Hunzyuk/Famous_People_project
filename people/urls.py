from django.urls import path

from people.views import index


app_name = 'people'


urlpatterns = [
    path('index/', index, name='index')
]
