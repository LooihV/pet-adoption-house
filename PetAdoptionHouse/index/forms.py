from django import forms
from .models import IdentificationType
from .models import User as UserCustom

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birthDate = forms.DateField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    adress = forms.CharField(max_length=100, required=False)
    identificationType = forms.ModelChoiceField(queryset=IdentificationType.objects.all())
    identificationDocument = forms.CharField(max_length=50, required=True)

    
    class Meta:
        model = UserCustom
        fields = ['email', 'password', 'first_name', 'last_name', 'birthDate', 'phone', 'adress', 'identificationType',
                  'identificationDocument']
        

