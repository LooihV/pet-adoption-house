from django.contrib import admin
from .models import *

admin.site.register([User, Role, IdentificationType, EmployeeInformation, Pet, Event, History, Adoption, Breed, Species])
