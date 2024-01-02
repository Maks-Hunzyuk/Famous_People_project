from django.contrib import admin

from people.models import People, Categories, TagPost, Partner

admin.site.register(People)
admin.site.register(Categories)
admin.site.register(TagPost)
admin.site.register(Partner)
