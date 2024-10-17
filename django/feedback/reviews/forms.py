from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label="Your name:",
#         required=True,
#         min_length=8,
#         max_length=50,
#         error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please enter a shorter name."
#         })
#     review_text = forms.CharField(
#         label="Your feedback:",
#         widget=forms.Textarea,
#         max_length=200
#     )
#     rating = forms.IntegerField(
#         label="Your rating:",
#         min_value=1,
#         max_value=5
#     )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = "__all__"
        # exclude = ["user_name"]
        fields = ["user_name", "review_text", "rating"]
        labels = {
            "user_name": "Your name:",
            "review_text": "Your Feedback:",
            "rating": "Rating:"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_lenght": "Please enter a shorter name!"
            }
        }
        help_texts = {
            "user_name": "Some useful help text.",
        }
