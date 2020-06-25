from django import forms
from profiles.models import UserProfile
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('agent_role', 'status', 'date')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'start_time': 'Start time',
            'end_time': 'end_time',
            'user_id': 'User',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = True