from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, date

from profiles.models import UserProfile
from .models import Coaching
from .forms import SessionForm


@login_required
def coaching(request):
    """
    Show the coaching sessions
    - Agents: Can see their own sessions
    - Managers: Can select the agent from their own team, and do all CRUD operations on the sessions
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    team = str(profile.team)

    if profile.level == 'manager':
        users_select = UserProfile.objects.filter(company_id=profile.company_id, team__team_name__icontains=team)
        if 'sel_agent' not in request.session:
            agent = str(users_select[0].user_id)
            request.session['sel_agent'] = agent

        if 'agent' in request.GET:
            agent = request.GET['agent']
            request.session['sel_agent'] = agent

        coachings = Coaching.objects.filter(user_id=request.session['sel_agent'])

        # Send full name to template for the Agent-selector
        get_sel_agent = get_object_or_404(UserProfile, pk=request.session['sel_agent'])
        full_name = get_sel_agent.first_name + " " + get_sel_agent.last_name

    elif profile.level == 'agent':
        coachings = Coaching.objects.filter(user_id=profile.user_id)

    else:
        messages.error(request, 'Only Managers and Agents have access to the Coaching-section')
        return redirect(reverse('planning'))

    template = 'coaching/coaching.html'
    context = {
        'coaching': coachings,
        'users_select': users_select,
        'current_agent': full_name,
        'profile': profile
    }

    return render(request, template, context)


@login_required
def add_session(request):
    """
    Add a new coaching session
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # make sure only managers can add coaching sessions
    if profile.level == 'manager':

        if request.method == 'POST':
            form = SessionForm(request.POST)
            if form.is_valid():
                get_sel_agent = get_object_or_404(UserProfile, pk=request.session['sel_agent'])
                session = form.save(commit=False)
                session.user_id = get_sel_agent
                session.manager = profile.first_name + " " + profile.last_name
                session.date = date.today()
                session.save()
                messages.success(request, 'Coaching session added successfully')

            else:
                messages.error(request, 'Update failed. Please ensure the form is valid.')

            coachings = Coaching.objects.filter(user_id=request.session['sel_agent'])
            # Send full name to template to show Agent
            get_sel_agent = get_object_or_404(UserProfile, pk=request.session['sel_agent'])
            full_name = get_sel_agent.first_name + " " + get_sel_agent.last_name

            template = 'coaching/coaching.html'
            context = {
                'coaching': coachings,
                'profile': profile,
                'current_agent': full_name,
            }
            return render(request, template, context)

        else:
            form = SessionForm()
            coachings = Coaching.objects.filter(user_id=request.session['sel_agent'])
            # Send full name to template to show Agent
            get_sel_agent = get_object_or_404(UserProfile, pk=request.session['sel_agent'])
            full_name = get_sel_agent.first_name + " " + get_sel_agent.last_name

            template = 'coaching/add_session.html'
            context = {
                'form': form,
                'profile': profile,
                'coaching': coachings,
                'current_agent': full_name
            }

    else:
        messages.error(request, "Sorry, you are not authorized to delete coaching sessions. Ask a manager.")
    
    return render(request, template, context)


@login_required
def edit_session(request, session_id):
    """
    Edit a coaching session
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # only managers can edit/add/delete coaching sessions
    if profile.level == 'manager':
        session = get_object_or_404(Coaching, pk=session_id)

        if request.method == 'POST':
            form = SessionForm(request.POST, instance=session)
            if form.is_valid():
                form.save()
                messages.success(request, 'Coaching session edited successfully')

                coachings = Coaching.objects.filter(user_id=request.session['sel_agent'])
                # Send full name to template to show Agent
                get_sel_agent = get_object_or_404(UserProfile, pk=request.session['sel_agent'])
                full_name = get_sel_agent.first_name + " " + get_sel_agent.last_name
    
                template = 'coaching/coaching.html'
                context = {
                    'coaching': coachings,
                    'profile': profile,
                    'current_agent': full_name,
                }
                return render(request, template, context)

            else:
                messages.error(request, 'Save failed. Please ensure the form is valid.')

                return redirect(reverse('coaching', ))

        else:
            form = SessionForm()
            coachings = Coaching.objects.filter(user_id=request.session['sel_agent'])
            # Send full name to template to show Agent
            get_sel_agent = get_object_or_404(UserProfile, pk=request.session['sel_agent'])
            full_name = get_sel_agent.first_name + " " + get_sel_agent.last_name

            template = 'coaching/edit_session.html'
            context = {
                'form': form,
                'profile': profile,
                'coaching': coachings,
                'current_agent': full_name,
                'session_selected': session
            }

            return render(request, template, context)

    else:
        messages.error(request, "Sorry, you are not authorized to edit coaching sessions. Ask a manager")

        return redirect(reverse('coaching', ))


def delete_session(request, session_id):
    """
    Delete a coaching session
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.level == 'manager':
        session = get_object_or_404(Coaching, pk=session_id)
        session.delete()
        messages.success(request, 'Coaching session deleted')

    else:
        messages.error(request, "Sorry, you are not authorized to delete coaching sessions. Ask a manager.")

    return redirect(reverse('coaching', ))
