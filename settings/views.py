from django.shortcuts import render


def settings_global(request):
    """ A view to return the index page """
    return render(request, 'settings/settings_global.html')


def settings_team(request):
    """ A view to return the index page """
    return render(request, 'settings/settings_team.html')
