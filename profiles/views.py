from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import UserProfile, User
from settings.models import Team, AgentRole  # Used to save a new created user profile
from django.contrib import messages
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
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
            # doesnt work yet: Email is not saved:

        if user_email.is_valid():
            user_email.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
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
    profile = get_object_or_404(UserProfile, user=request.user)
    users = UserProfile.objects.filter(company_id=profile.company_id)

    template = 'profiles/user_management.html'
    context = {
        'users': users,
        'profile': profile
    }
    return render(request, template, context)


@login_required
def add_user(request):
    """
    Add a new user, through menu point 'user management'
    visible to admins and managers
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only managers and admins can add a team
    if profile.level == 'admin' or profile.level == 'manager':

        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            user_email = UserForm(request.POST)

            if user_email.is_valid() and form.is_valid():
                user = User.objects.create_user(username=random_username(),
                                     email=request.POST.get('email'),
                                     password='EggBox')
                messages.success(request, 'Profile added successfully')

                user.userprofile.first_name = form.data['first_name']
                user.userprofile.last_name = form.data['last_name']
                user.userprofile.company_id = profile.company_id
                user.userprofile.start_date = form.data['start_date']
                user.userprofile.end_date = form.data['end_date']
                user.userprofile.level = form.data['level']
                user.userprofile.team = Team.objects.get(pk=form.data['team'])
                user.userprofile.contract_type = form.data['contract_type']
                user.userprofile.contract_percentage = form.data['contract_percentage']
                user.userprofile.agent_goal = form.data['agent_goal']
                user.userprofile.save()
            else:
                messages.error(request, 'Update failed. Please ensure the form is valid.')

            users = UserProfile.objects.filter(company_id=profile.company_id)

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
    else:
        messages.info(request, "Sorry, you are not authorized to add users. Ask a Manager or Admin.")

    return redirect(reverse('planning', ))


def random_username():
    """
    Generate a random unique username
    """
    return str(uuid.uuid4().hex.upper())


@login_required
def edit_user(request, user_id):
    """
    Edit a user, through menu point 'user management'
    visible to Admins and Managers
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only managers and admins can add a team
    if profile.level == 'admin' or profile.level == 'manager':

        user = get_object_or_404(UserProfile, pk=user_id)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'User edited successfully')

                users = UserProfile.objects.filter(company_id=profile.company_id)
                template = 'profiles/user_management.html'
                context = {
                    'users': users,
                    'profile': profile
                }
                return render(request, template, context)

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

    else:
        messages.info(request, "Sorry, you are not authorized to edit users. Ask a Manager or Admin.")

    return redirect(reverse('planning', ))


@login_required
def delete_user(request, user_id):
    """
    Delete a user
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # make sure only admins and managers can delete a team
    if profile.level == 'admin' or profile.level == 'manager':
        user = get_object_or_404(UserProfile, pk=user_id)

        # check that there is at least 1 admin
        if user.level == 'admin':
            admins = UserProfile.objects.filter(company_id=profile.company_id, level='admin')
            if len(admins) > 1:
                user.delete()
                messages.success(request, 'User deleted!')
                return redirect(reverse('planning', ))

            else:
                messages.error(request, "Delete failed: There has to be at least one Admin. Go to the global settings if you wish to delete the company account completely")
                return redirect(reverse('planning', ))
        
        else:
            user.delete()
            messages.success(request, 'User deleted!')
            return redirect(reverse('planning', ))

    else:
        messages.info(request, "Sorry, you are not authorized to delete teams. Ask a Manager or Admin.")

    return redirect(reverse('teams', ))


    return redirect(reverse('planning', ))