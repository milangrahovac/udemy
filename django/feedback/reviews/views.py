from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
# Create your views here.


# def review(request):
#     if request.method == "POST":
#         entered_username = request.POST["username"]

#         if entered_username == "" and len(entered_username) > 20:
#             return render(request, "reviews/review.html", {
#                 "has_error": True
#             })

#         return HttpResponseRedirect("/thank-you")

#     return render(request, "reviews/review.html", {
#         "has_error": False
#     })

# def review(request):
#     if request.method == "POST":
#         # existing_model = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_model)

#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             # Not need if using ".ModelForm"
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"]
#             # )
#             review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })


# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "thank-you"

# # save from if valid
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"
    # fields = "__all__"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# class ReviewsList(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

class ReviewsList(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"  # default object_list

    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    context_object_name = "review"  # default object

# check session if the article is favorite
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context

# add to favorites


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        # fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
