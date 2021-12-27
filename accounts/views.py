from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        pwd1 = request.POST['password']
        pwd2 = request.POST['password2']
        email = request.POST['email']

        if pwd1 == pwd2:
            #check for dup users
            if User.objects.filter(username=username).exists():
                messages.error(request, "This user already exists dimwit")
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exits dimwit!!!!')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,password=pwd1,email=email,first_name=first_name
                                                ,last_name=last_name)
                # auth.login(request,user)
                # messages.success("Logged In smart kid")
                # return redirect('index')
                user.save()
                messages.success(request,'Successfully logged in')
                return redirect('login')
        else:
            messages.error(request, 'Wrong password dimwit')
            return redirect(register)
    else:
        return render(request, 'accounts/register.html')

def login (request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Dimwit, you gotta stop trying")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You are out fosho")
        return redirect('login')

def dashboard (request):
    return render(request, 'accounts/dashboard.html')