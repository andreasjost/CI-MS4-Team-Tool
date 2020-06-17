from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from .models import Event, EventCategory
from django.core import serializers  # used to use template variables in JS
import datetime



def planning(request):
    """
    Get the logged in user profile and show the planning template
    and submit the current month+year
    """
    # set the session variable for month and year
    if 'sel_month' not in request.session:
        now = datetime.datetime.now()
        request.session['sel_month'] = now.month-1
        request.session['sel_year'] = now.year
    template = 'planning/planning.html'
    context = render_data(request)

    return render(request, template, context)


def month_plus(request):
    """ user pushed one month ahead in the planning """
    month = request.session['sel_month']
    year = request.session['sel_year']
    month += 1
    if month == 12:
        month = 0
        year += 1
    request.session['sel_month'] = month
    request.session['sel_year'] = year

    template = 'planning/planning.html'
    context = context = render_data(request)

    return render(request, template, context)


def month_minus(request):
    """ user pushed one month back in the planning """
    month = request.session['sel_month']
    year = request.session['sel_year']
    month -= 1
    if month == -1:
        month = 11
        year -= 1
    request.session['sel_month'] = month
    request.session['sel_year'] = year
    template = 'planning/planning.html'
    context = context = render_data(request)

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


def render_data(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    users = serializers.serialize("json", UserProfile.objects.all())

    now_json = '{"month": "%s", "year": "%s"}' % (request.session['sel_month'], request.session['sel_year'])

    template = 'planning/planning.html'
    context = {
        'profile': profile,
        'users': users,
        'mmyyyy': now_json
    }

    return context
