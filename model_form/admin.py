from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "birth_date"]


@admin.register(Book)
class BookOrderAdmin(admin.ModelAdmin):
    fields = ["name", "authors"]
    list_display = ["name", "get_authors"]
