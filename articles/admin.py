from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.TabularInline):
    model=Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Article)
admin.site.register(Comment)

# Register your models here.
