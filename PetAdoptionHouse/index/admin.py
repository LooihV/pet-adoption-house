from django.contrib import admin
from .models import *

admin.site.register([User, IdentificationType, Pet, Event, Adoption, Breed, Species])
