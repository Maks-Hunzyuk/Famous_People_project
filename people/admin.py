from django.contrib import admin

from people.models import People, Categories, TagPost, Partner


admin.site.register(TagPost)
admin.site.register(Partner)


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", 'category')
    list_display_links = ("id", "title")
    ordering = ("time_create", "title")
    list_editable = ('is_published',)
    list_per_page = 10


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
