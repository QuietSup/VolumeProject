from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from users.forms import SignupForm, LoginForm, UpdateUserForm
from django.contrib.auth.decorators import login_required
from Volume.models import User
from django.utils.text import slugify


# Create your views here.
def signup_view(request):
    print(request)
    print(request.method)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # log the user
            user = form.save()
            login(request, user)
            return redirect('users:edit_profile')
        else:
            print(form.error_messages)
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:edit_profile')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('users:edit_profile')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'users/edit-profile.html', {'user': request.user, 'form': form})

def logout_view(request):
    print(request)
    if request.method == 'POST':
        logout(request)
        return redirect('users:login')

def profile(request, slug, user_id):

    user = get_object_or_404(User, pk=user_id)

    if slugify(user.username) != slug:
        return redirect('users:profile', slug=slugify(user.username), user_id=user_id)

    return render(request, 'users/profile.html', {'user': user})