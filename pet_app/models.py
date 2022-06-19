from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Pet(models.Model):
    name = models.CharField(
        max_length=100, help_text='Enter the name of the pet')
    photo_url = models.ImageField(upload_to='images')
    breed = models.ManyToManyField(
        'Breed', help_text='Select the breed of the pet')
    born = models.DateField(null=True, help_text='Enter the date of birth')
    gender = models.ManyToManyField('Gender')
    favorite_snack = models.TextField(null=True)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(
        max_length=100, help_text='Enter the breed (e.g. Labrador)')

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender
