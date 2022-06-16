from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(
        max_length=100, help_text='Enter the name of the pet')
    photo_url = models.ImageField(upload_to='images')
    breed = models.ManyToManyField(
        'Breed', help_text='Select the breed of the pet')
    age = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(
        max_length=100, help_text='Enter the breed (e.g. Labrador)')

    def __str__(self):
        return self.name
