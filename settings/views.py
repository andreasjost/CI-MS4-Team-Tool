from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from profiles.models import UserProfile, CompanyProfile
from .models import Team, Shift
from .forms import CompanyProfileForm, TeamsForm, ShiftForm

import stripe


def settings_global(request):
    """
    Show the global settings According to the company id
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

    else:
        form = CompanyProfileForm(instance=company)

    template = 'settings/settings_global.html'
    context = {
        'profile': profile,
        'company': company,
        'form_company': form,
    }

    return render(request, template, context)


def change_plan(request):
    """
    Show the global settings According to the company id
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    profile = get_object_or_404(UserProfile, user=request.user)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

    if request.method == 'POST':
        data = request.POST
        try:
            company.plan = data['plan']
            company.payment = data['payment']
            company.renewal_date = datetime.date.today()
            # company.save()
            messages.success(request, 'Event changed successfully')

        except IndexError:
            messages.error(request, 'An error occured')

    else:
        form = CompanyProfileForm(instance=company)

    # Something needs to happen here
    stripe_total = 100

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'settings/change_plan.html'
    context = {
        'profile': profile,
        'company': company,
        'form_company': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def teams(request):
    """
    Show all teams related to the company
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    teams = Team.objects.filter(company_id=profile.company_id)

    template = 'settings/teams.html'
    context = {
        'teams': teams,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def add_team(request):
    """
    Add a new team
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # put some logic that only managers and admins can add a user
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """

    if request.method == 'POST':
        form = TeamsForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.company_id = profile.company_id
            team.save()
            # messages.success(request, 'Profile updated successfully')

        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')

        teams = Team.objects.filter(company_id=profile.company_id)

        template = 'settings/teams.html'
        context = {
            'teams': teams,
            'profile': profile
        }
        return render(request, template, context)

    else:
        form = TeamsForm()
        teams = Team.objects.filter(company_id=profile.company_id)

        template = 'settings/add_team.html'
        context = {
            'form': form,
            'profile': profile,
            'teams': teams
        }

        return render(request, template, context)


@login_required
def edit_team(request, team_id):
    """ Edit a team, out of teams """

    """ check the user level
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    team_selected = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        form = TeamsForm(request.POST, instance=team_selected)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team edited successfully')
            teams = Team.objects.filter(company_id=profile.company_id)
            template = 'settings/teams.html'
            context = {
                'teams': teams,
                'profile': profile
            }
            return render(request, template, context)

        else:
            messages.error(request, 'Save failed. Please ensure the form is valid.')
    else:
        form = TeamsForm(instance=team_selected)

    teams = Team.objects.filter(company_id=profile.company_id)
    template = 'settings/edit_team.html'
    context = {
        'form': form,
        'teams': teams,
        'team_selected': team_selected,
        'profile': profile
    }

    return render(request, template, context)


def delete_team(request, team_id):
    """
    Delete a team after checking if no users are attached
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if profile.level == 'admin' or profile.level == 'manager':
        users = UserProfile.objects.filter(company_id=profile.company_id, team=team_id)
        if len(users) == 0:
            team = get_object_or_404(Team, pk=team_id)
            team.delete()
            messages.success(request, 'Team deleted!')

        else:
            messages.error(request, "Users are still part of this team. Attach users to a different team in 'User Management' or delete them.")

    else:
        messages.error(request, "Sorry, you are not authorized to delete teams. Ask a Manager or Admin.")

    return redirect(reverse('teams', ))


def shifts(request):
    """
    Show all shifts related to the company, sorted by team
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    shifts = Shift.objects.filter(company_id=profile.company_id)

    template = 'settings/shifts.html'
    context = {
        'shifts': shifts,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def edit_shift(request, shift_id):
    """ Edit a role, out of the roles """

    """ check the user level
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    shift_selected = get_object_or_404(Shift, pk=shift_id)

    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift_selected)
        if form.is_valid():
            form.save()
            messages.success(request, 'Shift edited successfully')
            shifts = Shift.objects.filter(company_id=profile.company_id)
            template = 'settings/shifts.html'
            context = {
                'shifts': shifts,
                'profile': profile
            }
            return render(request, template, context)

        else:
            messages.error(request, 'Save failed. Please ensure the form is valid.')
    else:
        form = ShiftForm(instance=shift_selected)

    shifts = Shift.objects.filter(company_id=profile.company_id)
    template = 'settings/edit_shift.html'
    context = {
        'form': form,
        'shifts': shifts,
        'shift_selected': shift_selected,
        'profile': profile
    }

    return render(request, template, context)


@login_required
def add_shift(request):
    """
    Add a new role
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # put some logic that only managers and admins can add a user
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """

    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            shift = form.save(commit=False)
            shift.company_id = profile.company_id
            shift.save()
            messages.success(request, 'Shift added successfully')

        else:
            messages.error(request, 'Save failed. Please ensure the form is valid.')

        shifts = Shift.objects.filter(company_id=profile.company_id)

        template = 'settings/shifts.html'
        context = {
            'shifts': shifts,
            'profile': profile
        }
        return render(request, template, context)

    else:
        form = ShiftForm()
        shifts = Shift.objects.filter(company_id=profile.company_id)

        template = 'settings/add_shift.html'
        context = {
            'form': form,
            'profile': profile,
            'shifts': shifts
        }

        return render(request, template, context)
