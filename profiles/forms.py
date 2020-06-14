from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'company_id', )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name(s)',
            'last_name': 'Last Name',
            'birthday_ddmm': 'Birthday Day/Month',
            'start_date': 'Start date',
            'end_date': 'End date',
            'level': 'Authentication level',
            'role': 'Role',
            'team': 'Team',
            'contract_type': 'Contract Type',
            'contract_percentage': 'Contract Percentage',
            'agent_goal': 'State an overall goal',

        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            self.fields[field].label = placeholder


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email Address',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1 profile-form-input'
            self.fields[field].label = placeholder
