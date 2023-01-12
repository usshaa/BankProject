from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, UserApplicationForm
from .models import UserApplication


# Create your views here.
def homePage(request):
    return render(request,'myapp/home.html')


def registerPage(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'myapp/registration.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'myapp/registration.html', {'form': form})


def loginPage(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'myapp/login.html', {'form':form})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            msg = 'Username and password is wrong'
            form = LoginForm(request.POST)
            context={'form':form,'msg':msg}
            return render(request,'myapp/login.html',context)


def landingPage(request):
    return render(request,'myapp/landingpage.html')


def application(request):
    userapplication = UserApplication.objects.all()
    form = UserApplicationForm()
    if (request.method == 'POST'):
        form = UserApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('message')
    if (request.method == 'GET'):
        context = {'userapllication': userapplication, 'form': form}
        return render(request, 'myapp/form.html', context)


def messagePage(request):
    return render(request,'myapp/message.html')