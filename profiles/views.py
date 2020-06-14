from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import UserProfile, User
from .forms import UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required


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
    """ Add a user 
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
    """


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