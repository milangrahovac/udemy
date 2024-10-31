from django import forms
from .models import Participant


# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = ["first_name", "last_name", "email"]


class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First name:")
    last_name = forms.CharField(label="Last name:")
    email = forms.EmailField(label="Email:")
