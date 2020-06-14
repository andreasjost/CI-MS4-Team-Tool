from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField
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
    level = models.CharField(max_length=16, null=False, default='admin')
    role = models.CharField(max_length=32, null=True, blank=True)  # this will be a foreign key to the roles table
    team = models.CharField(max_length=32, null=True, blank=True)  # this will be a foreign key to the teams table
    contract_type = models.CharField(max_length=32, null=True, blank=True)
    contract_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    agent_goal = models.CharField(max_length=256, null=True, blank=True)
    company_id = models.CharField(max_length=32, null=False, editable=False)


class CompanyProfile(models.Model):
    """
    A company profile model created on sign up with the admin account
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='user_made_profile')
    company_name = models.CharField(max_length=80, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    plan = models.CharField(max_length=40, null=True, blank=True)
    signup_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    renewal_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    payment = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    # global settings: On what weekday does the week start
    setting_weekstart = models.DecimalField(max_digits=1, decimal_places=0, default=0)


@receiver(post_save, sender=User)
def create_update_user_profile(sender, instance, created, **kwargs):
    print("################")
    print("#  sender")
    print(sender)
    print("#  instance")
    print(instance)
    print("#  created")
    print(created)
    print("#  kwargs")
    print(kwargs)
    print("################")

    # Create or update the user profile
    if created:
        UserProfile.objects.create(user=instance)
        
    # Existing users: just save the profile
    instance.userprofile.save()
    

