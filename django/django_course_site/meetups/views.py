from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    meetups = Meetup.objects.all()
    return render(request, "meetups/index.html", {
        "show_meetups": True,
        "meetups": meetups
    })


# def meetup_details(request, meetup_slug):

#     try:
#         selected_meetup = meetups = Meetup.objects.get(slug=meetup_slug)
#         registration_form = RegistrationForm()
#         return render(request, "meetups/meetup-details.html", {
#             "meetup_found": True,
#             "meetup": selected_meetup,
#             "form": registration_form
#         })

#     except Exception as exc:
#         return render(request, "meetups/meetup-details.html", {
#             "meetup_found": False
#         })


# def meetup_details(request, meetup_slug):

#     try:
#         selected_meetup = meetups = Meetup.objects.get(slug=meetup_slug)

#         if request.method == "GET":
#             registration_form = RegistrationForm()
#         elif request.method == "POST":
#             registration_form = RegistrationForm(request.POST)
#             if registration_form.is_valid():
#                 user_email = registration_form.cleaned_data["email"]
#                 first_name = registration_form.cleaned_data["first_name"]
#                 last_name = registration_form.cleaned_data["first_name"]

#                 participant, _ = Participant.objects.get_or_create(
#                     email=user_email,
#                     first_name=first_name,
#                     last_name=last_name
#                 )
#                 selected_meetup.participants.add(participant)
#                 return redirect("confirm-registration", meetup_slug=meetup_slug)

#         return render(request, "meetups/meetup-details.html", {
#             "meetup_found": True,
#             "meetup": selected_meetup,
#             "form": registration_form
#         })

#     except Exception as exc:
#         return render(request, "meetups/meetup-details.html", {
#             "meetup_found": False
#         })


def meetup_details(request, meetup_slug):

    try:
        selected_meetup = meetups = Meetup.objects.get(slug=meetup_slug)

        if request.method == "GET":
            registration_form = RegistrationForm()
        elif request.method == "POST":
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data["email"]
                first_name = registration_form.cleaned_data["first_name"]
                last_name = registration_form.cleaned_data["last_name"]

                try:
                    participant, _ = Participant.objects.get_or_create(
                        email=user_email,
                        first_name=first_name,
                        last_name=last_name
                    )
                except Exception as e:

                    return render(request, "meetups/meetup-details.html", {
                        "meetup_found": True,
                        "meetup": selected_meetup,
                        "form": registration_form,
                        "registration_error": True
                    })

                selected_meetup.participants.add(participant)
                return redirect("confirm-registration", meetup_slug=meetup_slug)

        return render(request, "meetups/meetup-details.html", {
            "meetup_found": True,
            "meetup": selected_meetup,
            "form": registration_form
        })

    except Exception as exc:
        return render(request, "meetups/meetup-details.html", {
            "meetup_found": False
        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, "meetups/registration-sucess.html", {
        "title": meetup.title,
        "organizer_email": meetup.organizer_email,
    })
