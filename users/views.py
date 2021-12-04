from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileModelForm, UserUpdateForm
from django.contrib import messages
from blog.models import BlogPost

def profile_view(request):
    user = request.user
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=user)

    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'user': user,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'user/profile_view.html', context)

def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-view')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'user/update.html', context)