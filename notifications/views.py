from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from .models import Notification


def notifications(request):
    """
    Show all notifications
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    notifications = Notification.objects.filter(user_id=profile.user_id)

    template = 'notifications/notifications.html'
    context = {
        'notifications': notifications,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def delete_message(request, message_id):
    """
    Delete a message
    """
    message = get_object_or_404(Notification, pk=message_id)
    message.delete()
    messages.success(request, 'Message deleted!')

    return redirect(reverse('notifications', ))
