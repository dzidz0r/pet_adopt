from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name='pets'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.form, name='form'),
]
