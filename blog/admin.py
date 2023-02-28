from django.contrib import admin

from blog.models import Comment, Post


# Register your models here.
@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created", "date_updated", "author")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "date_created"]
