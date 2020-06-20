from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile, CompanyProfile
from .models import Team, AgentRole, Shift
from .forms import CompanyProfileForm, TeamsForm, AgentRoleForm


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
            # messages.success(request, 'Profile updated successfully')
        else:
            print("unsuccessful")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')

    else:
        form = CompanyProfileForm(instance=company)

    template = 'settings/settings_global.html'
    context = {
        'profile': profile,
        'company': company,
        'form_company': form
    }

    return render(request, template, context)


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
            print("unsuccessful team save")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')

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
            print("Success")
            teams = Team.objects.filter(company_id=profile.company_id)
            template = 'settings/teams.html'
            context = {
                'teams': teams,
                'profile': profile
            }
            return render(request, template, context)

        else:
            print("failed")
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


def delete_team(request):

    # Show user management
    profile = get_object_or_404(UserProfile, user=request.user)
    teams = Team.objects.filter(company_id=profile.company_id)

    template = 'settings/teams.html'
    context = {
        'teams': teams,
        'profile': profile
    }
    return render(request, template, context)


def roles(request):
    """
    Show all roles related to the company
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    roles = AgentRole.objects.filter(company_id=profile.company_id)

    template = 'settings/roles.html'
    context = {
        'roles': roles,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def edit_role(request, role_id):
    """ Edit a role, out of the roles """

    """ check the user level
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    role_selected = get_object_or_404(AgentRole, pk=role_id)

    if request.method == 'POST':
        form = AgentRoleForm(request.POST, instance=role_selected)
        if form.is_valid():
            form.save()
            print("Success")
            roles = AgentRole.objects.filter(company_id=profile.company_id)
            template = 'settings/roles.html'
            context = {
                'roles': roles,
                'profile': profile
            }
            return render(request, template, context)

        else:
            print("failed")
    else:
        form = AgentRoleForm(instance=role_selected)

    roles = AgentRole.objects.filter(company_id=profile.company_id)
    template = 'settings/edit_role.html'
    context = {
        'form': form,
        'roles': roles,
        'role_selected': role_selected,
        'profile': profile
    }

    return render(request, template, context)


@login_required
def add_role(request):
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
        form = AgentRoleForm(request.POST)
        if form.is_valid():
            role = form.save(commit=False)
            role.company_id = profile.company_id
            role.save()
            # messages.success(request, 'Profile updated successfully')

        else:
            print("unsuccessful role save")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')

        roles = AgentRole.objects.filter(company_id=profile.company_id)

        template = 'settings/roles.html'
        context = {
            'roles': roles,
            'profile': profile
        }
        return render(request, template, context)

    else:
        form = AgentRoleForm()
        roles = AgentRole.objects.filter(company_id=profile.company_id)

        template = 'settings/add_role.html'
        context = {
            'form': form,
            'profile': profile,
            'roles': roles
        }

        return render(request, template, context)


def shifts(request):
    """
    Show all shifts related to the company, sorted by team
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    shifts = Shift.objects.filter() # add filter for the teams of the same company

    template = 'settings/shifts.html'
    context = {
        'shifts': shifts,
        'profile': profile
    }
    return render(request, template, context)
