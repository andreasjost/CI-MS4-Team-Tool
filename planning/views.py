from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from .models import Event, EventCategory
from django.core import serializers  # used to use template variables in JS


def planning(request):
    """
    Get the logged in user profile and show the planning template
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # users = UserProfile.objects.all()

    users = serializers.serialize("json", UserProfile.objects.all())

    template = 'planning/planning.html'
    context = {
        'profile': profile,
        'users': users
    }

    return render(request, template, context)


def summary(request, user_id):
    """ Display the user's summary. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(UserProfile, pk=user_id)

    template = 'planning/summary.html'
    context = {
        'profile': profile,
        'user': user
    }

    return render(request, template, context)
