from django.contrib import admin
from livlearn.api.models import Link, Tag


class LinkAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)