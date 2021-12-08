from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User


def register(request):
    # this form will create user by data which we sent in Post method OR in Get method it will return an empty form
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # validated data of form will store in cleaned_data (as you know!)
            username = form.cleaned_data.get('username')
            # this is a flash message of django
            messages.success(request, f'Your account has been created! now you are able to Login.')
            return redirect('login')

    return render(request, 'users/register.html', {'form': form})


@login_required  # The user must be logged in to see this view and url
def profile(request):
    return render(request, 'users/profile.html')


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html', context)


class PasswordResetViewNew(PasswordResetView):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        try:
            User.objects.get(email=email)
            return super(PasswordResetViewNew, self).post(request, *args, **kwargs)
        except User.DoesNotExist:
            # this for if the email is not in the db of the system
            messages.error(request, f'Your entered email was not found!')
            return redirect('password_reset')
