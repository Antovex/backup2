from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return HttpResponse("Hello home")

def errorpage(request):
    return HttpResponse("Bad Credentials")

def signin(request):
    if request.method == "POST":
        name = request.POST['name']
        pass1 = request.POST['password']
        # print("got details")
        user = authenticate(username=name, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # print("Bad ceds")
            messages.error(request, "Bad Credentials")
            # ask what to do here
            return redirect('errorpage')



    return render(request, 'signin/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        print("Your account has been successfully created")

        messages.success(request, "Your account has been successfully created")
        return redirect('signin')

    return render(request, 'signin/register.html')

def signout(request):
    pass