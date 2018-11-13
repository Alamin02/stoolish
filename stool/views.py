from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from .forms import RegistrationForm, RecievePost
from .models import Post

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
    user = User.objects.get(username=username)
    query = Post.objects.filter(user__exact=user)
    return render(request, 'user/profile.html', {'posts': query})

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
        else:
            return render(request,'registration/signup.html' , {'error' : 'Invalid Credentials!', 'form':form })
    else:
        form = RegistrationForm
        return render(request, 'registration/signup.html', {'form': form})

def post_on_wall(request, username):
    if request.method == 'POST':
        form = RecievePost(request.POST)
        user = User.objects.get(username=username)
        post = Post(user=user, message=form.data['message'])
        if form.is_valid:
            post.save()
            context = {
                'user' : user,
                'form' : form,
                'message' : 'success',
            }
            return render(request, 'user/post.html', context)
        else:
            context = {
                'user' : user,
                'form' : form,
                'message' : 'failed',
            }
            return render(request, 'user/post.html', context)
    else:
        person = get_object_or_404(User, username=username)
        form = RecievePost
        context = {
            'user' : person,
            'form' : form
        }
        return render(request, 'user/post.html', context)