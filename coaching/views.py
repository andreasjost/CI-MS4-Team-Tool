from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from .models import Coaching


@login_required
def coaching(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    coachings = Coaching.objects.filter(user_id=profile.user_id)

    template = 'coaching/coaching.html'
    context = {
        'coaching': coachings,
        'profile': profile
    }
    return render(request, template, context)
