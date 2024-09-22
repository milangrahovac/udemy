from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Eat no chocolate for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Jango for at least 20 minutes every day!",
    "april": "Learn Kubernetes for at least 20 minutes every day!",
    "may": "Learn Docker for at least 20 minutes every day!",
    "june": "Learn Go for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Play Nitendo for at least 20 minutes every day!",
    "september": "Play Xbox for at least 20 minutes every day!",
    "october": "Learn Python for at least 20 minutes every day!",
    "november": "Learn Python and Kubernetes for at least 30 minutes every day!",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        # OR
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month == 0 or month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)
