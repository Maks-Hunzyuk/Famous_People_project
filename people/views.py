from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404

from people.models import People, Categories, TagPost
from people.forms import AddPostForm


menu = [
    "О сайте",
    "Добавить статью",
    "Обратная связь",
    "Войти",
]


def index(request):
    posts = People.published.all().select_related('category')
    context = {
        "menu": menu,
        "title": "Главная страница",
        "posts": posts,
        "category_selected": 0,
    }
    return render(request, "people/index.html", context)


def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)

    context = {"title": post.title, "menu": menu, "post": post, "category_selected": 1}
    return render(request, "people/post.html", context)


def show_category(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    posts = People.published.filter(category_id=category.pk).select_related('category')
    context = {
        "title": f"Рубрика: {category.name}",
        "menu": menu,
        "posts": posts,
        "category_selected": category.pk,
    }

    return render(request, "people/index.html", context)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.changed_data)
    else:
        form = AddPostForm()
    context = {
        'menu': menu,
        'title': 'Добавление статью',
        'form': form
    }
    return render(request, 'people/addpage.html', context)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def about(request):
    context = {"title": "О сайте"}
    return render(request, "people/about.html", context)


def  show_tag_post_list(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=People.Status.PUBLISHED).select_related('category')

    context = {
        'title': f"Тег: #{tag.tag}",
        'menu': menu,
        'posts': posts,
        'category_selected': None
    }
    return render(request, 'people/index.html', context)
 