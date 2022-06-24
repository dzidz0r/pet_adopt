from django.shortcuts import render, redirect
from .form_register import RegisterForm, authenticate, login
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            confirm_password = form.cleaned_data.get('password2')
            user = authenticate(
                username=username, password=raw_password, confirm=confirm_password)
            login(request, user)
            messages.success(
                request, 'Account was successfully created for ' + username)

        return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('your_pass')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, 'templates/home.html', {'username': username})

        else:
            messages.error(request, 'Bad credentials')
            return redirect('/')
    return render(request, "registration/login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/')
