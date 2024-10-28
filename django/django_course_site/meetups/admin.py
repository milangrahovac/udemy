from django.contrib import admin
from .models import Meetup, Location

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address", )


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", )
    list_filter = ("location", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Location, LocationAdmin)
admin.site.register(Meetup, MeetupAdmin)
