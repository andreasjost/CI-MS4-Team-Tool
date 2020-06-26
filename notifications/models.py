from django.db import models
from profiles.models import UserProfile


class Notification(models.Model):
    """
    Notifications are sent to users
    """
    user_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    message_sender = models.CharField(max_length=80)
    date = models.DateField()
    message_text = models.CharField(max_length=200)
