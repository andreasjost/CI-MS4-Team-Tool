from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile updated successfully')
        else:
            print("unsuccessful")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True,
        'profile': profile
    }

    return render(request, template, context)

"""
def thankyou(request):
    # Page to display after sign up of a new account

    template = 'profiles/thankyou.html'

    return render(template)
"""