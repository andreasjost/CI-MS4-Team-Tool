# newly created to customize allauth forms
"""
from django.contrib.auth import get_user_model
"""
from profiles.models import UserProfile
from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'plan', 'signup-date', 'renewal-date', 'payment')
        
   



"""
class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
"""