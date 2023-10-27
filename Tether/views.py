from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
        
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        fname, lname = fullname.split()
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        role = request.POST.get('role')

        print(fname, username,  lname, email, pwd1, pwd2, role)

        if pwd1!=pwd2 or User.objects.filter(username=username).exists():
            messages.info(request, 'Hey there, fill out the info properly!')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, first_name=fname, last_name=lname, password=pwd1, email=email)
            user.save()
            Profile.objects.create(user=user, role=role)

            user = authenticate(username=username, password=pwd1)
            login(request, user)

            return redirect('/')
    return render(request, 'register.html')

def loginUser(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Take the L and login again')
            return render(request, 'login.html')
    # No backend authenticated the credentials
    return render(request, 'login.html')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
