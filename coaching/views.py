from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from .models import Coaching


@login_required
def coaching(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.level == 'manager':
        coachings = Coaching.objects.filter(user_id=profile.user_id)
    
    elif profile.level == 'agent':
        coachings = Coaching.objects.filter(user_id=profile.user_id)

    template = 'coaching/coaching.html'
    context = {
        'coaching': coachings,
        'profile': profile
    }
    return render(request, template, context)
