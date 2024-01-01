from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти',]
url_name = ['about', 'add_page', 'contact', 'login']


data_db = [
    {'id': 1, 'title': 'Аднжелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Роббертс', 'content': 'Биография Джулии Роббертс', 'is_published': True}
]

def index(request):
    context = {
               'menu': menu,
               'title': 'Главная страница',
               'posts': data_db,
               'url_name': url_name
               }
    return render(request, 'people/index.html', context)

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id {post_id}')

def add_page(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def about(request):
    context = {'title': 'О сайте'}
    return render(request, 'people/about.html', context)
