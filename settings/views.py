from django.shortcuts import render, get_object_or_404

from settings.models import CompanyProfile


def settings_global(request, company_id):
    """ Show the global settings According to the company id
    """

    company = get_object_or_404(CompanyProfile, pk=company_id)

    context = {
        'company': company,
    }

    return render(request, 'settings/settings_global.html', context)


def settings_team(request):
    """ show the team settings """
    return render(request, 'settings/settings_team.html')
