from django.contrib import admin
from .models import Author, Post, Tag, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date",)
    list_filter = ("author", "tags", "date",)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "post")
    list_filter = ("user_name", "user_email", "post")


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
