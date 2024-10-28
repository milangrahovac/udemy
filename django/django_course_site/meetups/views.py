from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {
        "show_meetups": True,
        "meetups": meetups
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {
        "title": "A First Meetup",
        "location": "New York",
        "slug": "a-first-meetup",
        "description": "This is the first meetup!"
    }
    try:
        selected_meetup = meetups = Meetup.objects.get(slug=meetup_slug)
        return render(request, "meetups/meetup-details.html", {
            "meetup_found": True,
            "meetup_title": selected_meetup.title,
            "meetup_description": selected_meetup.description,
        })

    except Exception as exc:
        return render(request, "meetups/meetup-details.html", {
            "meetup_found": False
        })
