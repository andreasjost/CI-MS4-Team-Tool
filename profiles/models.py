from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


"""
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):

    # Create or update the user profile

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
"""
