from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
