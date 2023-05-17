from django import forms
from .models import IdentificationType
from .models import User as UserCustom

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birth_date = forms.DateField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    adress = forms.CharField(max_length=100, required=False)
    identificationType = forms.ModelChoiceField(queryset=IdentificationType.objects.all())
    identificationDocument = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = UserCustom
        fields = ['email', 'first_name', 'last_name', 'birth_date', 'phone', 'adress', 'identificationType',
                  'identificationDocument']
        

