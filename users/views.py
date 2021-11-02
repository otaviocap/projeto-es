from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from posts.models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Sua conta foi criada, agora só logar :)')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'start-page/register.html', {'form': form})

@login_required
def follow(request, username):
    if request.method == "POST":
        user = get_object_or_404(User, username=username)
        if (request.user is not None):
            if (request.user not in user.profile.followers.all()):
                print("adding")                
                user.profile.followers.add(request.user)
                request.user.profile.following.add(user)
            else:
                print("Removing")
                user.profile.followers.remove(request.user)
                request.user.profile.following.remove(user)

    return render(request, 'goBack.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'social/edit.html', context)