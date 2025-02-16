from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'category', 'created_at', 'count_views', 'get_photo')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'tags')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm
    save_on_top = True
    readonly_fields = ('count_views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content','photo', 'get_photo', 'count_views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    get_photo.short_description = 'Фото'
    get_photo.allow_tags = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

