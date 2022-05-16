from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UpdateUserForm


@login_required
def profile(request):
    """ view for updating user information in profiles app """
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'profiles/profiles.html', {'user_form': user_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    """ view to enable users to update or change their password """
    template_name = 'profiles/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = "profiles/"
