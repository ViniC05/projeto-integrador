from django.contrib import admin

from .models import Category, portal


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(portal)
class PostAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
