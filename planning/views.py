from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from settings.models import Team
from .models import Event
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
    


def month_change(request, new_month):
    """
    user pushed one month forward or back
    
    --- YEAR BREAK DOESN'T WORK. FIX IT ---
    
    """
    # month = request.session['sel_month']
    year = request.session['sel_year']
    if new_month > 12:
        new_month = 0
        year += 1
    if new_month < 0:
        new_month = 11
        year -= 1
    request.session['sel_month'] = new_month
    request.session['sel_year'] = year

    template = 'planning/planning.html'
    context = render_data(request)

    return render(request, template, context)


def month_current(request):
    """
    Reset the month
    """
    now = datetime.datetime.now()
    request.session['sel_month'] = now.month-1
    request.session['sel_year'] = now.year
    template = 'planning/planning.html'
    context = render_data(request)

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
    teams = Team.objects.filter(company_id=profile.company_id)

    team=''

    if 'team' in request.GET:
        team = request.GET['team']
    
    elif profile.level == 'agent' or profile.level == 'manager':
        team = profile.team
    
    else:
        team = "The best team"
    

    users = serializers.serialize("json", UserProfile.objects.filter(company_id=profile.company_id))
    # users = serializers.serialize("json", UserProfile.objects.filter(company_id=profile.company_id, team__team_name__in=team))


    now_json = '{"month": "%s", "year": "%s"}' % (request.session['sel_month'], request.session['sel_year'])
    navmonth = {
        'previous': request.session['sel_month'] - 1,
        'next': request.session['sel_month'] + 1
    }

    context = {
        'profile': profile,
        'users': users,
        'teams': teams,
        'current_team': team,
        'mmyyyy': now_json,
        'nav_month': navmonth
    }

    return context
