# users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Profil oluştur
            login(request, user)  # Kaydolunca otomatik giriş
            return redirect("profile")  # Profil sayfasına yönlendir
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def explore_profiles(request):
    # Giriş yapan kullanıcı hariç tüm profilleri getir
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'users/explore_profiles.html', {"users": users})

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/user_profile.html', {"profile_user": user})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Başarıyla güncellenince profil sayfasına yönlendir
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'form': form
    }
    return render(request, 'profile_update.html', context)