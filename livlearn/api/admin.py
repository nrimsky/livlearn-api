from django.contrib import admin
from livlearn.api.models import Test


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)