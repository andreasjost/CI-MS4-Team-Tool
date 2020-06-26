from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from settings.models import Team, AgentRole
import datetime


class UserProfile(models.Model):
    """
    A user profile model for a user account (any user)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    birthday_ddmm = models.CharField(max_length=16, null=False, default='0000')
    start_date = models.DateField(null=False, default=datetime.date.today)
    end_date = models.DateField(null=False, default=datetime.date.today)

    level_choices = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('agent', 'Agent'),
        ('visitor', 'Visitor'),
    )
    level = models.CharField(max_length=16, null=False,
                             default='admin', choices=level_choices)

    # Only Agents have a role assigned
    # Roles are currently disabled
    role = models.ForeignKey(AgentRole, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='agent_role')

    # Only Agents and Managers have a role assigned
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='team_member')
    # only Agents and Managers have a contract type
    contract_choices = (
        ('hour', 'Paid by the hour'),
        ('fix', 'Fix contract'),
    )
    contract_type = models.CharField(max_length=16, null=False,
                                     default='admin', choices=contract_choices)
    contract_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    agent_goal = models.CharField(max_length=256, null=True, blank=True)
    company_id = models.CharField(max_length=32, null=False, editable=False)


class CompanyProfile(models.Model):
    """
    A company profile model created on sign up with the admin account
    """
    company_id = models.CharField(max_length=32, null=False, editable=False)
    company_name = models.CharField(max_length=80, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    plan = models.CharField(max_length=40, null=False, blank=False, default="starter")
    signup_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    renewal_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    payment = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    # global settings: On what weekday does the week start
    setting_daystart = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    setting_dayend = models.DecimalField(max_digits=2, decimal_places=0, default=24)


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):
    print("{################")
    print("#  sender")
    print(sender)
    print("#  instance")
    print(instance)
    print("#  created")
    print(created)
    print("#  kwargs")
    print(kwargs)
    print("################}")

    # Create user profile
    if created:
        UserProfile.objects.create(user=instance)

    # Existing users: just save the profile
    instance.userprofile.save()
