from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import UserProfile, User
from .forms import UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required
import uuid


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        user_email = UserForm(instance=request.user)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile updated successfully')
        else:
            print("unsuccessful")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')
        
        # doesnt work yet: Email is not saved:

        if user_email.is_valid():
            user_email.save()
            # messages.success(request, 'Profile updated successfully')
        else:
            print("####### unsuccessful email")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
        user_email = UserForm(instance=request.user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'user_email': user_email,
        'on_profile_page': True,
        'profile': profile
    }

    return render(request, template, context)


def user_management(request):

    # Show user management
    users = UserProfile.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/user_management.html'
    context = {
        'users': users,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def add_user(request):
    """
    Add a user 
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    # put some logic that only managers and admins can add a user
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """

    if request.method == 'POST':

        form = UserProfileForm(request.POST)
        user_email = UserForm(request.POST)

        if user_email.is_valid() and form.is_valid():
            user = User.objects.create_user(username=random_username(),
                                 email=request.POST.get('email'),
                                 password='glass onion')
            # messages.success(request, 'Profile updated successfully')

            first_name = form.data['first_name']
            last_name = form.data['last_name']
            # company_id = self._generate_company_id() -- take it from the company profile
            user.userprofile.first_name = first_name
            user.userprofile.last_name = last_name
            user.userprofile.company_id = profile.company_id

            user.userprofile.save()
        else:
            print("unsuccessful email")
            # messages.error(request, 'Update failed. Please ensure the form is valid.')

        
        users = UserProfile.objects.all()

        template = 'profiles/user_management.html'
        context = {
            'users': users,
            'profile': profile
        }
        return render(request, template, context)

    else:
        form = UserProfileForm()
        user_email = UserForm()

        template = 'profiles/add_user.html'
        context = {
            'form': form,
            'profile': profile,
            'user_email': user_email
        }

        return render(request, template, context)


def random_username():
        """
        Generate a random unique username
        """
        return str(uuid.uuid4().hex.upper())
    


@login_required
def edit_user(request, user_id):
    """ Edit a user, out of user management """

    """ check the user level
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    """
    user = get_object_or_404(UserProfile, pk=user_id)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            print("Success")
            """
            return redirect(reverse('product_detail', args=[product.id]))
            """
        else:
            print("failed")
    else:
        form = UserProfileForm(instance=user)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': user,
    }

    return render(request, template, context)

"""
def thankyou(request):
    # Page to display after sign up of a new account

    template = 'profiles/thankyou.html'

    return render(template)
"""