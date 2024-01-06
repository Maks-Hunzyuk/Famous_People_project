from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView

from .models import People, TagPost, UploadFile
from .forms import AddPostForm, UploadFileForm


menu = [
    "О сайте",
    "Добавить статью",
    "Обратная связь",
    "Войти",
]


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            item = UploadFile(file=form.changed_data["file_upload"])
            item.save()
    else:
        form = UploadFileForm()
    context = {"title": "О сайте", "form": form}
    return render(request, "people/about.html", context)


class AddPageView(View):
    def get(self, request):
        form = AddPostForm()
        context = {
            "menu": menu,
            "title": "Добавление статьи",
            "form": form,
        }

        return render(request, "people/addpage.html", context)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("people:home")
        context = {"menu": menu, "title": "Добавление статьи", "form": form}
        return render(request, "people/addpage.html", context)


class IndexTemplateView(ListView):
    # model = People
    template_name = "people/index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return People.published.all().select_related("category")


class PeopleCategoryView(ListView):
    template_name = "people/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return People.published.filter(
            category__slug=self.kwargs["category_slug"]
        ).select_related("category")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        item = context["posts"][0].category
        context["title"] = "Категория - " + item.name
        context["menu"] = menu
        context["category_selected"] = item.pk
        return context


class TagPostListView(ListView):
    template_name = "people/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])
        context["title"] = "Тег:" + tag.tag
        context["menu"] = menu
        context["category_selected"] = None
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return People.published.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("category")


class ShowPostView(DetailView):
    model = People
    template_name = "people/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = context["post"].title
        context["menu"] = menu
        return context

    def get_object(self, queryset: QuerySet[Any] | None = ...):
        return get_object_or_404(
            People.published, slug=self.kwargs[self.slug_url_kwarg]
        )
