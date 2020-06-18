from django import forms
from profiles.models import CompanyProfile
from settings.models import Team


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ('company_id',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company name',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'country': 'Country or State',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'plan': 'Plan',
            'signup_date': 'Date Signed up',
            'renewal_date': 'Last Plan renewal',
            'payment': 'Paid for number of months',
            'setting_weekstart': 'The Day your week starts'
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = placeholder


class TeamsForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ('company_id',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'company_name': 'Company name',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'country': 'Country or State',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'plan': 'Plan',
            'signup_date': 'Date Signed up',
            'renewal_date': 'Last Plan renewal',
            'payment': 'Paid for number of months',
            'setting_weekstart': 'The Day your week starts'
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = placeholder