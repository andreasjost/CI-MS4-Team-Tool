from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile, CompanyProfile
from settings.models import Team
from django.contrib import messages
from .models import Event
from notifications.models import Notification
from django.core import serializers  # used to use template variables in JS
from datetime import datetime, timedelta, date
import json


@login_required
def planning(request):
    """
    Get the logged in user profile and show the planning template
    and submit the current month+year
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    teams = Team.objects.filter(company_id=profile.company_id)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

    if request.method == 'POST':
        data = request.POST

        # in case of edit event
        if 'event_id' in data:
            event_selected = get_object_or_404(Event, pk=data['event_id'])

            # connect event to correct user
            sel_user = get_object_or_404(UserProfile, user_id=data['user_id'])

            try:
                event_selected.category = data['category']
                event_selected.start_time = data['start_time']
                event_selected.end_time = data['end_time']
                event_selected.user_id = sel_user
                event_selected.save()
                messages.success(request, 'Event changed successfully')

            except IndexError:
                messages.error(request, 'An error occured')

        # in case of new event
        else:

            # construct the date
            sel_day = int(data['day'])
            sel_month = int(request.session['sel_month'])
            sel_year = int(request.session['sel_year'])
            date_sel = datetime(sel_year, sel_month, sel_day)

            # connect event to correct user
            sel_user = get_object_or_404(UserProfile, user_id=data['user_id'])

            try:
                Event.objects.create(
                    category=data['category'],
                    date=date_sel,
                    start_time=data['start_time'],
                    end_time=data['end_time'],
                    user_id=sel_user,
                    status=data['status'],
                )

                messages.success(request, 'Event created successfully')

                # create a message in case a manager/admin created an event for another user
                if profile.user_id != sel_user.user_id:
                    full_name = profile.first_name + " " + profile.last_name
                    Notification.objects.create(
                        message_sender=full_name,
                        date=date.today(),
                        message_text="A '" + data['category'] + "'-event has been created on " + str(date_sel),
                        user_id=sel_user
                    )

            except IndexError:
                messages.success(request, 'An error occured')

        return redirect(reverse('planning', ))

    else:

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
            request.session['sel_team'] = team

        elif profile.level == 'agent' or profile.level == 'manager':
            team = str(profile.team)
            if 'sel_team' not in request.session:
                request.session['sel_team'] = team

        else:
            team = str(teams[0])
            if 'sel_team' not in request.session:
                request.session['sel_team'] = team

        users_select = UserProfile.objects.filter(company_id=profile.company_id, team__team_name__icontains=request.session['sel_team'])
        events_filtered = Event.objects.filter(date__month=sel_month, date__year=sel_year)

        # preparing data to read in JS
        js_month = int(request.session['sel_month'])-1
        users = serializers.serialize("json", users_select)
        events = serializers.serialize("json", events_filtered)
        now_json = '{"month": "%s", "year": "%s"}' % (js_month, request.session['sel_year'])
        dayspan_json = '{"start": "%s", "end": "%s"}' % (company.setting_daystart, company.setting_dayend)

        template = 'planning/planning.html'

        context = {
            'profile': profile,
            'users_select': users_select,
            'users': users,
            'teams': teams,
            'current_team': request.session['sel_team'],
            'mmyyyy': now_json,
            'daySpan': dayspan_json,
            'nav_month': navmonth,
            'events': events
        }

        return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """
    delete an event from the planning
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    event = get_object_or_404(Event, pk=event_id)
    sel_user = event.user_id
    event_category = event.category
    event_date = event.date
    event.delete()
    messages.success(request, 'Event deleted!')

    # create a message in case a manager/admin deleted an event of another user

    if profile.user_id != sel_user.user_id:
        full_name = profile.first_name + " " + profile.last_name
        Notification.objects.create(
            message_sender=full_name,
            date=date.today(),
            message_text="A '" + event_category + "'-event has been deleted on " + str(event_date),
            user_id=sel_user
        )

    return redirect(reverse('planning', ))


    """ add some if-statements
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home')) 
    """


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


def copy_event(request):
    """
    view called after user has selected target day(s) to copy events to
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    selected_user = str(profile.user_id)

    if profile.level == 'admin' or profile.level == 'manager':
        selected_user = request.POST['selected_user']

    # get the selected days from JS
    selected_days = json.loads(request.POST['selected_days'])

    # get the events to copy from the 'source'-day
    sel_month = int(request.session['sel_month'])
    sel_year = int(request.session['sel_year'])
    sel_day = int(selected_days[0])
    events_filtered = Event.objects.filter(date__month=sel_month,
                                           date__year=sel_year,
                                           date__day=sel_day,
                                           user_id=selected_user)
    for i in range(1, len(selected_days)):

        # 1. delete existing events in the 'target'-days
        events_clear = Event.objects.filter(date__month=sel_month,
                                            date__year=sel_year,
                                            date__day=selected_days[i],
                                            user_id=selected_user)
        events_clear.all().delete()

        # 2. Copy an event to the new date
        for j in events_filtered:
            date_sel = j.date
            date_new = date_sel.replace(day=int(selected_days[i]))
            Event.objects.create(
                    category=j.category,
                    date=date_new,
                    start_time=j.start_time,
                    end_time=j.end_time,
                    user_id=j.user_id,
                    status=j.status,
            )

    return redirect(reverse('planning', ))
