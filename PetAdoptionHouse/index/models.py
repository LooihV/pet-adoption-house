from django.db import models

class EmployeeInformation(models.Model):
    department = models.CharField(max_length=20)
    salary = models.FloatField()

class Role(models.Model):
    employeeInformation = models.BooleanField()
    employeeInformationId = models.ForeignKey(EmployeeInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

class IdentificationType(models.Model):
    name = models.CharField(max_length=10)
    
class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    identificationType = models.ForeignKey(IdentificationType, on_delete=models.CASCADE)
    identificationDocument = models.CharField(max_length=50)
    birthDate = models.DateField()
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)

