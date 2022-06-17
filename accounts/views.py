from django.shortcuts import render, redirect
from .form_register import RegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})
