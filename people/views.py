from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения People")

def categories(request, category_id):
    return HttpResponse(f"<h1>Страница с категориями</h1><p>id: {category_id}")

def categories_by_slug(request, category_slug):
    return HttpResponse(f"<h1>Страница с категориями</h1><p>slug: {category_slug}")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}")
