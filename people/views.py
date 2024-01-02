from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404

from people.models import People


menu = [
    "О сайте",
    "Добавить статью",
    "Обратная связь",
    "Войти",
]
url_name = ["about", "add_page", "contact", "login"]


data_db = [
    {
        "id": 1,
        "title": "Аднжелина Джоли",
        "content": "Биография Анджелины Джоли",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Марго Робби",
        "content": "Биография Марго Робби",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Джулия Роббертс",
        "content": "Биография Джулии Роббертс",
        "is_published": True,
    },
]

categories_db = [
    {"id": 1, "name": "Актрисы"},
    {"id": 2, "name": "Актеры"},
    {"id": 3, "name": "Спортсмены"},
    {"id": 4, "name": "Спортсменки"},
]


def index(request):
    posts = People.published.all()
    context = {
        "menu": menu,
        "title": "Главная страница",
        "posts": posts,
        "url_name": url_name,
        "category_selected": 0,
    }
    return render(request, "people/index.html", context)


def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)

    context = {"title": post.title, "menu": menu, "post": post, "category_selected": 1}
    return render(request, "people/post.html", context)


def show_category(request, category_id):
    context = {
        "title": "Отображние по категориям",
        "menu": menu,
        "posts": data_db,
        "category_selected": category_id,
    }

    return render(request, "people/index.html", context)


def add_page(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def about(request):
    context = {"title": "О сайте"}
    return render(request, "people/about.html", context)
