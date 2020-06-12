from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for a user account
    """
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    birthday_ddmm = models.CharField(max_length=16, null=False, default='0000')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    level = models.CharField(max_length=16, null=False, default='admin')
    role = models.CharField(max_length=32, null=True, blank=True)  # this will have to become a foreign key to the roles table
    team = models.CharField(max_length=32, null=True, blank=True)  # this will have to become a foreign key to the teams table
    contract_type = models.CharField(max_length=32, null=True, blank=True)
    contract_percentage = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    agent_goal = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.email


class CompanyProfile(models.Model):
    """
    A company profile model created on sign up with the admin account
    """
    company_name = models.CharField(max_length=80, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    plan = models.CharField(max_length=40, null=True, blank=True)
    signup_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    renewal_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    payment = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return self.company_name


class AgentRole(models.Model):
    """
    Manager defined roles (ie intern, junior, medior, senior)
    """
    role_name = models.CharField(max_length=80)
    role_color = models.IntegerField()

    def __str__(self):
        return self.role_name


"""
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):

    # Create or update the user profile

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
"""
