from typing import Any

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import AddPostForm
from .models import People, TagPost
from .utils import DataMixin


def contact(request):
    return HttpResponse("Обратная связь")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


@login_required
def about(request):
    contact_list = People.published.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"title": "О сайте", "page_obj": page_obj}
    return render(request, "people/about.html", context)


class AddPageView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = "people/addpage.html"
    success_url = reverse_lazy("people:home")
    title_page = 'Добавление статьи'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

class UpdatePageView(DataMixin, UpdateView):
    model = People
    fields = ('title', 'content', 'photo', 'is_published', 'category')
    success_url = reverse_lazy('people:home')
    title_page = 'Редактирование статьи'


class IndexTemplateView(DataMixin, ListView):
    template_name = "people/index.html"
    title_page = 'Главная страница'
    category_selected = 0

    def get_queryset(self) -> QuerySet[Any]:
        return People.published.all().select_related("category")


class PeopleCategoryView(DataMixin, ListView):
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
        return self.get_mixin_context(context,
                                      title='Категория - ' + item.name,
                                      category_selected=item.pk)


class TagPostListView(DataMixin, ListView):
    template_name = "people/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])
        return self.get_mixin_context(context, title='Тег:'+tag.tag)

    def get_queryset(self) -> QuerySet[Any]:
        return People.published.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("category")


class ShowPostView(DataMixin, DetailView):
    model = People
    template_name = "people/post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset: QuerySet[Any] | None = ...):
        return get_object_or_404(
            People.published, slug=self.kwargs[self.slug_url_kwarg]
        )
