from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfilesForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.


# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfilesForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submitted_form = ProfilesForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             # store_file(request.FILES["image"])
#             return HttpResponseRedirect("/profiles")
#         return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })


class CreateProfileView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
