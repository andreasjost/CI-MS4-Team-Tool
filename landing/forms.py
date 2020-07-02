from django import forms
from profiles.models import CompanyProfile
from settings.models import Team, AgentRole, Shift
import uuid
import datetime


class SignupForm(forms.Form):

    def _generate_company_id(self):
        """
        Generate a random, unique number using UUID to link
        all functions to the right company
        """
        return uuid.uuid4().hex.upper()

    def signup(self, request, user):
        company_id = self._generate_company_id()

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']

        """
        1. Create a user profile
        """
        user.save()
        user.refresh_from_db()
        user.userprofile.company_id = company_id
        user.userprofile.first_name = first_name
        user.userprofile.last_name = last_name

        """
        2. Create a company profile
        """
        CompanyProfile.objects.create(
            company_name=company_name,
            company_id=company_id,
            signup_date=datetime.date.today()
        )

        """
        3. Create 1 initial team
        """

        Team.objects.create(
            team_name='The best team',
            planning_deadline=14,
            coaching_rep=1,
            min_lunchbreak=30,
            min_dinnerbreak=30,
            min_paidbreak=15,
            company_id=company_id
        )

        """
        4. Create initial roles
        """
        AgentRole.objects.create(
            role_name='Intern',
            role_color='ff9966',
            company_id=company_id
        )
        AgentRole.objects.create(
            role_name='Junior',
            role_color='66ffb3',
            company_id=company_id
        )
        AgentRole.objects.create(
            role_name='Medior',
            role_color='66b3ff',
            company_id=company_id
        )
        AgentRole.objects.create(
            role_name='Senior',
            role_color='ff66ff',
            company_id=company_id
        )

        """
        5. Create sample shifts
        """
        Shift.objects.create(
            shift_name='Day Shift',
            min_agents=2,
            shift_start="08:00",
            shift_end="20:00",
            weekday_sunday=True,
            weekday_monday=True,
            weekday_tuesday=True,
            weekday_wednesday=True,
            weekday_thursday=True,
            weekday_friday=True,
            weekday_saturday=True,
            company_id=company_id
        )

        Shift.objects.create(
            shift_name='Night Shift',
            min_agents=2,
            shift_start="20:00",
            shift_end="22:00",
            weekday_sunday=True,
            weekday_monday=True,
            weekday_tuesday=True,
            weekday_wednesday=True,
            weekday_thursday=True,
            weekday_friday=True,
            weekday_saturday=True,
            company_id=company_id
        )