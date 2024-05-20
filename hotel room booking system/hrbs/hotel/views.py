from django.shortcuts import render
from userauth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html')

def rooms(request):
    return render(request, 'rooms.html')

def about(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "about.html", {"username": username})
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request,'index.html')


def booking(request):
    return render(request,'booking.html')
