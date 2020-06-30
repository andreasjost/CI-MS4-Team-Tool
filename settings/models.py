from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Team(models.Model):
    """
    List of the different teams
    """
    company_id = models.CharField(max_length=32, null=False, editable=False)
    team_name = models.CharField(max_length=64, null=False, blank=False, default="Teamname")
    planning_deadline = models.IntegerField(default=0)
    coaching_rep = models.IntegerField(default=0)
    min_lunchbreak = models.IntegerField(default=30)
    min_dinnerbreak = models.IntegerField(default=30)
    min_paidbreak = models.IntegerField(default=15)

    def __str__(self):
        return self.team_name


class AgentRole(models.Model):
    """
    Manager defined roles (default: intern, junior, medior, senior)
    This Model is currently not used due to deadline pressure
    """
    role_name = models.CharField(max_length=64)
    role_color = models.CharField(max_length=6)
    company_id = models.CharField(max_length=32, null=False, editable=False)

    def __str__(self):
        return self.role_name


class Shift(models.Model):
    """
    Different kinds of work shifts at different times
    """
    company_id = models.CharField(max_length=32, null=False, editable=False)
    shift_name = models.CharField(max_length=64, null=False, blank=False)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    min_agents = models.IntegerField(default=1)
    weekday_sunday = models.BooleanField(default=True)
    weekday_monday = models.BooleanField(default=True)
    weekday_tuesday = models.BooleanField(default=True)
    weekday_wednesday = models.BooleanField(default=True)
    weekday_thursday = models.BooleanField(default=True)
    weekday_friday = models.BooleanField(default=True)
    weekday_saturday = models.BooleanField(default=True)

    def __str__(self):
        return self.shift_name
