from django.contrib import admin
from . models import Pet, Breed, Gender

# Register your models here.
admin.site.register(Pet)
admin.site.register(Breed)
admin.site.register(Gender)
