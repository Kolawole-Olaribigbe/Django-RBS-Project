from django.shortcuts import render, redirect
from userauth.models import User, Profile
from django.contrib.auth import authenticate, login, logout
from hrbs import settings
from django.contrib import messages

# Create your views here.

# Register/Sign Up function
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        country = request.POST['country']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email):
            messages.error(request, "Account already exists")
            return redirect("sign_in")
        
        if password != password:
            messages.error(request, "Account does not exist")
            
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, country=country, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # authenticate user
        user = authenticate(email= email, password= password)
        login(request, user)
        messages.success(request, "Account created")
    
        return redirect('sign_in')
    
    else:
        return render(request, 'register.html',)

# Sign In/Log in function
def sign_in(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "home.html", {"username": username})
        else: 
            messages.error(request, "Wrong Password")
            return redirect("sign_in")
    return render(request, 'sign_in.html', {})


# Sign Out/logout function
def sign_out(request):
    logout(request)
    return redirect('index')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')
