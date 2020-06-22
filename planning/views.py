from django.shortcuts import render, redirect, reverse, get_object_or_404
from profiles.models import UserProfile, CompanyProfile
from settings.models import Team
from django.contrib import messages
from .models import Event
from django.core import serializers  # used to use template variables in JS
from datetime import datetime, timedelta


def planning(request):
    """
    Get the logged in user profile and show the planning template
    and submit the current month+year
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    teams = Team.objects.filter(company_id=profile.company_id)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)
    # set the session variable for month and year
    if 'sel_month' not in request.session:
        date_now = datetime.now()
        request.session['sel_month'] = date_now.month
        request.session['sel_year'] = date_now.year

    sel_month = int(request.session['sel_month'])
    sel_year = int(request.session['sel_year'])
    date_sel = datetime(sel_year, sel_month, 1)
    previous_month = date_sel + timedelta(days=-10)
    next_month = date_sel + timedelta(days=40)

    navmonth = {
        'previous': previous_month.month,
        'next': next_month.month,
        'current': request.session['sel_month']
    }

    if 'month' in request.GET:
        month = int(request.GET['month'])
        if month == 0:
            date_now = datetime.now()
            request.session['sel_month'] = date_now.month
            request.session['sel_year'] = date_now.year

            return redirect(reverse('planning'))

        else:
            year = int(request.session['sel_year'])
            if date_sel.month == 12 and month == 1:
                year += 1

            if date_sel.month == 1 and month == 12:
                year -= 1

            date_sel = date_sel.replace(month=month)
            previous_month = date_sel + timedelta(days=-10)
            next_month = date_sel + timedelta(days=40)

            request.session['sel_month'] = month
            request.session['sel_year'] = year

            return redirect(reverse('planning'))

    team = ''

    if 'team' in request.GET:
        team = request.GET['team']

    elif profile.level == 'agent' or profile.level == 'manager':
        team = profile.team

    else:
        team = teams[0]

    # code to pass data to JS
    js_month = int(request.session['sel_month'])-1
    users = serializers.serialize("json", UserProfile.objects.filter(company_id=profile.company_id, team__team_name__icontains=team))
    now_json = '{"month": "%s", "year": "%s"}' % (js_month, request.session['sel_year'])
    dayspan_json = '{"start": "%s", "end": "%s"}'% (company.setting_daystart, company.setting_dayend)

    template = 'planning/planning.html'
    context = {
        'profile': profile,
        'users': users,
        'teams': teams,
        'current_team': team,
        'mmyyyy': now_json,
        'daySpan': dayspan_json,
        'nav_month': navmonth
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
