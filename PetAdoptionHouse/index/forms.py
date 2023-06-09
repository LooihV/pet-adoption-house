from django import forms
from .models import IdentificationType, Adoption
from .models import User as UserCustom
from datetime import date

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

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
    
    class Meta:
        model = UserCustom
        fields = ['email', 'password', 'first_name', 'last_name', 'birthDate', 'phone', 'adress', 'identificationType',
                  'identificationDocument']
        
class AdoptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].initial = UserCustom.objects.filter(is_staff=True).first()

    employee = forms.ModelChoiceField(queryset=UserCustom.objects.filter(is_staff=True))
    date = forms.DateField(initial=date.today, widget=forms.DateInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Adoption
        fields = ['employee', 'date']
