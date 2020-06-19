from django.db import models
from profiles.models import UserProfile
from settings.models import AgentRole


class Event(models.Model):
    """
    Every entry in the calendar is an event
    """
    user_id = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    category_choices = (
        ('work', 'Work'),
        ('training', 'Training'),
        ('meeting', 'Meeting'),
        ('holidays', 'Holidays'),
        ('sick', 'Sick'),
        ('Leave', 'leave'),
        ('lunch', 'Lunch break'),
        ('dinner', 'Dinner break'),
        ('break', 'Paid break'),
        ('absence', 'Absence')
    )
    category = models.CharField(max_length=16, choices=category_choices)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    agent_role = models.ForeignKey(AgentRole, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    status = models.IntegerField()  # status of approvement

