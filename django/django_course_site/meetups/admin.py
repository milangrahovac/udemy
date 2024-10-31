from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address", )


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", )
    list_filter = ("email", )


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "organizer_email", )
    list_filter = ("location", "date", "organizer_email", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Location, LocationAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Meetup, MeetupAdmin)
