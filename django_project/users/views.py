from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import os
from django_project.settings import MEDIA_ROOT

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    general_current_user_img = User.objects.get(username=request.user.profile.user)
    general_current_user_img = general_current_user_img.profile.image.url
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            if general_current_user_img != '/media/default.jpg' and general_current_user_img != request.user.profile.image.url:
                os.unlink(os.path.join(
                    os.path.join(MEDIA_ROOT, request.user.profile.image.url.split('/')[-2]),
                    os.path.basename(general_current_user_img))
                )
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


@login_required
def reset_image(request):
    general_current_user_img = User.objects.get(username=request.user.profile.user)
    general_current_user_img = general_current_user_img.profile.image.url

    user_image = Profile.objects.filter(user_id=request.user.id)[0]
    if general_current_user_img != '/media/default.jpg':
        os.unlink(os.path.join(
            os.path.join(MEDIA_ROOT, request.user.profile.image.url.split('/')[-2]),
            os.path.basename(general_current_user_img))
        )
    user_image.image = 'default.jpg'
    user_image.save()
    return redirect('profile')
