from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post, Profile

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/home.html', { 'posts': posts })

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                age=form.cleaned_data.get('age'),
                gender=form.cleaned_data.get('gender')
            )
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'posts/signup.html', {'form': form})