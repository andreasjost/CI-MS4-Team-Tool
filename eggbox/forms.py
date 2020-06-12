# newly created to customize allauth forms.
# you have to de-comment:
# # ACCOUNT_SIGNUP_FORM_CLASS = 'eggbox.forms.SignupForm'
# in settings.py
"""
from django.contrib.auth import get_user_model
"""
from profiles.models import UserProfile
from settings.models import CompanyProfile

from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name')
