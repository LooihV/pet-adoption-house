from django.contrib import admin
from .models import User, Role, IdentificationType, EmployeeInformation

admin.site.register([User, Role, IdentificationType, EmployeeInformation])
