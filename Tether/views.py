from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile, Campaign
from django.contrib.auth import login, logout
from django.contrib import messages
import re

# Create your views here.

def index(request):
    user_role= 0
    for x in Profile.objects.filter(user = request.user):
        print(x, x.role)
        if not x.role == 'naive_user':
            print('working')
            user_role = 1
    return render (request, 'index.html', {'user_role': user_role})

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

        if User.objects.filter(username=username).exists():
            messages.info(request, f'Username {username} already exists :(')
            return redirect('/register')
        elif pwd1!=pwd2:
            messages.info(request, 'Passwords do not match!')
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
            messages.info(request, 'Incorrect username or password')
            return render(request, 'login.html')
    # No backend authenticated the credentials
    return render(request, 'login.html')

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    
def campaigns(request):
    user_role= 0
    for x in Profile.objects.filter(user = request.user):
        print(x, x.role)
        if not x.role == 'naive_user':
            print('working')
            user_role = 1

    campaigns_collection = Campaign.objects.all()

    context = {'user_role':user_role, 'campaigns':campaigns_collection}
    return render(request, 'campaigns.html', context)

def createCampaign(request):
    user_role= 0
    for x in Profile.objects.filter(user = request.user):
        if not x.role == 'naive_user':
            user_role = 1

    if request.method == 'POST':
        title = request.POST.get('title')
        campaign_type = request.POST.get('campaign-type')
        description = request.POST.get('description')
        doe = request.POST.get('DateofEvent')
        tags = request.POST.get('tags')
        tags_arr = re.findall(r'\w+', tags)

        bgimg = request.FILES.get('imagebg')
        contact_info = request.POST.get('c_info')

        # Use regular expressions to find phone numbers and email addresses
        phone_numbers = re.findall(r'\+?[0-9]+[-. ()]*[0-9]+[-. ()]*[0-9]+', contact_info)
        emails = re.findall(r'\S+@\S+', contact_info)

        # Clean up phone numbers and emails
        formatted_phone_numbers = []
        for number in phone_numbers:
            number = re.sub(r'[-. ()]', '', number)  # Remove unwanted characters
            if number.startswith('+'):
                formatted_phone_numbers.append(number)
            else:
                formatted_phone_numbers[-1] += number  # Append to the previous number

        emails = [email.replace(',', '') for email in emails]

        c_info = [formatted_phone_numbers, emails]

        Campaign.objects.create(title=title, campaign_type=campaign_type, description=description, doe=doe, tags_arr=tags_arr, bgimg=bgimg, contact_info=c_info)
        print(title, campaign_type, description, doe, tags_arr, c_info)
    return render(request, 'create.html', {'user_role': user_role})


def displayCampaign(request, id):
    req_campaign = Campaign.objects.filter(id=id)
    return render(request, 'display.html', {'campaign':req_campaign})
