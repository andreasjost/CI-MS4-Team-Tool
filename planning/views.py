from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from .models import Event, EventCategory


def planning(request):
    """
    Get the logged in user profile and show the planning template
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # users = get_object_or_404(UserProfile.objects.all())
    template = 'planning/planning.html'
    context = {
        'profile': profile,
        # 'users': users
    }

    return render(request, template, context)
