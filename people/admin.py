from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet

from people.models import People, Categories, TagPost, Partner


admin.site.register(TagPost)
admin.site.register(Partner)


class MarriedFilter(admin.SimpleListFilter):
    title = "Семейное положение"
    parameter_name = "status"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [("married", "В браке"), ("single", "Одинок")]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "married":
            return queryset.filter(partner__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(partner__isnull=True)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "time_create",
        "is_published",
        "category",
        "brief_info",
    )
    list_display_links = ("id", "title")
    ordering = ("time_create", "title")
    list_editable = ("is_published",)
    list_per_page = 10
    search_fields = ("title__startswith", "category__name")
    list_filter = (MarriedFilter, "category__name", "is_published")
    actions = ("set_published", "set_draft")

    @admin.display(description="Карткое описание", ordering="content")
    def brief_info(self, human: People):
        return f"Описание {len(human.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=People.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Удалить со страницы выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=People.Status.DRAFT)
        self.message_user(
            request, f"{count} Записей удалено со страницы", messages.WARNING
        )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
