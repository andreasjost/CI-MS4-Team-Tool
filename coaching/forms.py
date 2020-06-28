from django import forms

from .models import Coaching


class SessionForm(forms.ModelForm):
    class Meta:
        model = Coaching
        exclude = ('user_id', 'manager', 'date')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'field': 'Field (ie. Phone, Mails, Chat, etc)',
            'good': 'What was good?',
            'improve': 'Where is room for improvement?',
            'goal': "what's the goal until the next session?",
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
