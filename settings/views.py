from django.shortcuts import render, get_object_or_404

from profiles.models import CompanyProfile
from profiles.models import UserProfile


def settings_global(request):
    """ Show the global settings According to the company id
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile.company_id)
    company = get_object_or_404(CompanyProfile, company_id=profile.company_id)

    context = {
        'company': company,
    }

    return render(request, 'settings/settings_global.html', context)


def settings_team(request):
    """ show the team settings """
    return render(request, 'settings/settings_team.html')
