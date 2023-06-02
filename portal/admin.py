from django.contrib import admin

from .models import Category, portal


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(portal)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published', 'author']
    list_display_links = 'title', 'created_at',
    search_fields = 'id', 'title', 'description', 'slug', 'preparation_steps',
    list_filter = 'Category', 'author', 'is_published',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',)
    }


admin.site.register(Category, CategoryAdmin)
