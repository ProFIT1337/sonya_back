from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Room, Category


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'order_index')
    list_display = ('title', 'order_index')
    list_editable = ('order_index',)
    prepopulated_fields = ({'slug': ('title', )})


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('room', 'parent', 'title', 'slug', 'photo', 'get_photo', 'description', 'order_index')
    list_display = ('title', 'room', 'parent', 'get_photo', 'order_index')
    list_editable = ('order_index', )
    prepopulated_fields = ({'slug': ('title', )})
    readonly_fields = ('get_photo', )

    def get_photo(self, instance):
        if instance.photo:
            return mark_safe(f'<img src="{instance.photo.url}" width="200" />')
        return None

    get_photo.short_description = 'Фотография'
