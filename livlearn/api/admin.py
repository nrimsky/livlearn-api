from django.contrib import admin
from livlearn.api.models import Link, Tag, FormSubmission


class LinkAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class FormAdmin(admin.ModelAdmin):
    list_display = ("form_name", "submitted_at", "content")
    list_filter = ("submitted_at","form_name")
    search_fields = ("form_name__icontains","content__icontains")


admin.site.register(Link, LinkAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(FormSubmission, FormAdmin)