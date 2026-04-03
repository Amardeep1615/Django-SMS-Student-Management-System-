from django.contrib import admin
from .models import Blog,Comment
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title','blog_body']
    list_filter = ['blog_title','blog_body']
    search_fields = ['blog_title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment']
    list_filter = ['comment']
    search_fields = ['comment']