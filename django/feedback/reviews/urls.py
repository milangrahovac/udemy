from django.urls import path
from . import views

urlpatterns = [
    # path("", views.review),
    path("", views.ReviewView.as_view(), name="index"),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsList.as_view(), name="review-list"),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="single_review"),
]

# path("reviews/<int:id>", views.SingleReviewView.as_view(), name="single_review"),
