from django import forms
from profiles.models import CompanyProfile
from .models import Team, AgentRole, Shift


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ('company_id', 'plan', 'signup_date', 'renewal_date', 'payment')

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
            'payment': 'Paid for number of months',
            'setting_daystart': 'Hour when your day starts',
            'setting_dayend': 'hour when your day ends'
        }

        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field == 'setting_daystart' or field == 'setting_dayend' or field == 'payment':
                self.fields[field].widget.attrs['class'] = 'width-numbers'
            else:
                self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = placeholder


class TeamsForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = ('company_id',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'team_name': 'Team name',
            'planning_deadline': 'planning_deadline',
            'coaching_rep': 'coaching_rep',
            'min_lunchbreak': 'min_lunchbreak',
            'min_dinnerbreak': 'min_dinnerbreak',
            'min_paidbreak': 'min_paidbreak'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False


class AgentRoleForm(forms.ModelForm):
    class Meta:
        model = AgentRole
        exclude = ('company_id',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'role_name': 'Role name',
            'role_color': 'role color',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        exclude = ('company_id',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'shift_name': 'Shift name',
            'min_agents': 'Minimum Number of Agents',
            'shift_start': 'Start time',
            'shift_end': 'End time',
            'weekday_sunday': 'Sunday',
            'weekday_monday': 'Monday',
            'weekday_tuesday': 'Tuesday',
            'weekday_wednesday': 'Wednesday',
            'weekday_thursday': 'Thursday',
            'weekday_friday': 'Friday',
            'weekday_saturday': 'Saturday'
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
