from django.shortcuts import render
from .models import Pet

# Create your views here.


def home(request):
    return render(request, 'home.html')


def pets(request):
    pets = Pet.objects.all()

    return render(request, 'pets.html', {'pets': pets})


def contact(request):
    return render(request, 'contact.html')


def form(request):
    return render(request, 'form.html')
