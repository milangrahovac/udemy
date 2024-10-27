from django.contrib import admin
from .models import Meetups

# Register your models here.


class PostMeetups(admin.ModelAdmin):
    list_display = ("title", "slug", )
    list_filter = ("title", )
    prepopulated_fileds = {"slug": ("title",)}
    # verbose_name = 'Meetups'


admin.site.register(Meetups, PostMeetups)
# admin.site.register(Meetups)
