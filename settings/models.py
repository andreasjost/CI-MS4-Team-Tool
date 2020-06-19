from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Team(models.Model):
    """
    List of the different teams
    GLOBAL SETTING
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
    Manager defined roles (ie intern, junior, medior, senior)
    TEAM SETTING
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             null=True, blank=True, related_name='team_role')
    role_name = models.CharField(max_length=80)
    role_color = models.IntegerField()

    def __str__(self):
        return self.role_name


class Shift(models.Model):
    """
    Different kinds of work shifts at different times
    TEAM SETTING
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             null=True, blank=True, related_name='team_shift')
    shift_name = models.CharField(max_length=64, null=False, blank=False)
    weekday = models.IntegerField(default=0)
    shift_start = models.TimeField()
    shift_end = models.TimeField()

    def __str__(self):
        return self.shift_name
