from django.db import models


#---------- User models ----------
class EmployeeInformation(models.Model):
    department = models.CharField(max_length=20)
    salary = models.FloatField()
    def __str__(self) -> str:
        return self.department

class Role(models.Model):
    employeeInformation = models.BooleanField()
    employeeInformationId = models.ForeignKey(EmployeeInformation, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name

class IdentificationType(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name
    
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
    def __str__(self) -> str:
        return self.name


# --------------Pet Models------------------
class Breed(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=100)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.name

class Pet(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthDate = models.DateField()
    color = models.CharField(max_length=20)
    photo = models.CharField(max_length=300)
    gender = models.CharField(max_length=10)

# -------------- Adoption Models --------------


