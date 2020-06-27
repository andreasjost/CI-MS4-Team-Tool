from django.db import models
from profiles.models import UserProfile


class Coaching(models.Model):
    """
    Goals that managers set together with Agents
    """
    user_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    manager = models.CharField(max_length=80)
    date = models.DateField()
    field = models.CharField(max_length=40)
    good = models.CharField(max_length=200)
    improve = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
