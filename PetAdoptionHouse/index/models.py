from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as gtl
from datetime import date

#---------- User models ----------
class IdentificationType(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(gtl('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('birthDate', '2000-01-01')
        extra_fields.setdefault('phone', '1234567890')
        extra_fields.setdefault('adress', '1St. street')
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gtl('email adress'), unique=True)
    first_name = models.CharField(gtl('first name'), max_length=30, blank=True)
    last_name = models.CharField(gtl('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(gtl('active'), default=True)
    is_staff = models.BooleanField(gtl('staff status'), default=False)
    date_joined = models.DateTimeField(gtl('date joined'), auto_now_add=True)

    birthDate = models.DateField(null=True)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    identificationType = models.ForeignKey(IdentificationType, on_delete=models.CASCADE, null=True)
    identificationDocument = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return self.email
    
    def get_full_name(self) -> str:
        return str(self.first_name + " " + self.last_name)

    def get_short_name(self) -> str:
        return str(self.first_name)
    
    def calculate_age(self):
        today = date.today()
        birth_date = self.birthDate
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    


# --------------Pet Models------------------
class Breed(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Pet(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    birthDate = models.DateField()
    color = models.CharField(max_length=20)
    photo = models.CharField(max_length=300)
    gender = models.CharField(max_length=10)
    available = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
    def get_age(self):
        today = date.today()
        delta = today - self.birthDate

        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30

        age_components = []

        if years > 0:
            age_components.append(f"{years} {'years' if years > 1 else 'year'}")
        if months > 0:
            age_components.append(f"{months} {'months' if months > 1 else 'month'}")
        if days > 0:
            age_components.append(f"{days} {'days' if days > 1 else 'day'}")

        age_str = ' '.join(age_components)
        
        return age_str

# -------------- Adoption Models --------------

class Event(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Adoption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Adoptant")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Employee")
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="Event", default=None)
    date = models.DateField()
    def __str__(self) -> str:
        return f"Adoption #{str(self.id)}"

