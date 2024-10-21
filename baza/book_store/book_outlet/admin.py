from django.contrib import admin
from .models import Author
from .models import Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_filter = ("rating", "author",)
    list_display = ("title", "author",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
