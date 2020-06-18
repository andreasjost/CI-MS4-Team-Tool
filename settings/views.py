from django.shortcuts import render, get_object_or_404

from profiles.models import UserProfile, CompanyProfile
from .models import Team
from .forms import CompanyProfileForm


def settings_global(request):
    """
    Show the global settings According to the company id
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

    # use filter on teams: make object iterable even if there's only 1
    teams = Team.objects.filter(company_id=profile.company_id)

    if request.method == 'POST':
        form_company = CompanyProfileForm(request.POST, instance=company)
        if form_company.is_valid():
            form_company.save()
            # messages.success(request, 'Profile updated successfully')
        else:
            print("unsuccessful")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')

    else:
        form_company = CompanyProfileForm(instance=company)

    template = 'settings/settings_global.html'
    context = {
        'profile': profile,
        'company': company,
        'teams': teams,
        'form_company': form_company
    }

    return render(request, template, context)


def delete_team(request, team_id):
    """
    Delete a team and re-render the global settings
    """
    # warning message

    profile = get_object_or_404(UserProfile, user=request.user)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)
    teams = get_object_or_404(Team, company_id=profile.company_id)

    form = CompanyProfileForm(instance=company)

    template = 'settings/settings_global.html'
    context = {
        'profile': profile,
        'company': company,
        'teams': teams,
        'form': form
    }

    return render(request, template, context)


def settings_team(request):
    """
    show the team settings
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # company = get_object_or_404(CompanyProfile, company_id=profile.company_id)
    """
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
    """
    template = 'settings/settings_team.html'
    context = {
        'profile': profile,
        'company': company,
        'form': form
    }

    return render(request, template, context)
