from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'photo', 'get_photo', 'date', 'description', 'full_text', 'full_text_mobile')
    list_display = ('title', 'get_photo', 'date')
    readonly_fields = ('get_photo',)
    prepopulated_fields = ({'slug': ('title',)})

    def get_photo(self, instance):
        if instance.photo:
            return mark_safe(f'<img src="{instance.photo.url}" width="200" />')
        return None

    get_photo.short_description = 'Фотография'
