from django.contrib import admin

from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'created_at')
    list_filter = ['created_at', 'id']
    search_fields = ('title', 'category')
    filter_horizontal = ('tag', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_filter = ['created_at']
    readonly_fields = list_filter
    search_fields = ('name', 'email')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
