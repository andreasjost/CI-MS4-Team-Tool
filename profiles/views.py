from django.shortcuts import render

from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """

    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,

    }

    return render(request, template, context)


def thankyou(request):
    """ Page to display after sign up of a new account """

    template = 'profiles/thankyou.html'

    return render(template)
