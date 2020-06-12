from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


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

    # global settings: On what weekday does the week start
    setting_weekstart = models.DecimalField(max_digits=1, decimal_places=0, default=0)

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

class Team(models.Model):
    """
    Model for the different teams
    """
    team_name = models.CharField(max_length=64, null=False, blank=False, default="Teamname")
    planning_deadline = models.IntegerField(default=0)
    coaching_rep = models.IntegerField(default=0)
    min_lunchbreak = models.IntegerField(default=30)
    min_dinnerbreak = models.IntegerField(default=30)
    min_paidbreak = models.IntegerField(default=15)

