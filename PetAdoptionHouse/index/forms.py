from django import forms
from .models import IdentificationType, Adoption, Event
from .models import User as UserCustom
from datetime import date

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birthDate = forms.DateField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    address = forms.CharField(max_length=100, required=True)
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
    employee = forms.ModelChoiceField(queryset=UserCustom.objects.filter(is_staff=True), widget=forms.HiddenInput(), required=False)
    date = forms.DateField(widget=forms.HiddenInput(), required=False, initial=date.today())
    status = forms.ModelChoiceField(queryset=Event.objects.filter(name='Pending'), widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Adoption
        fields = ['employee', 'date', 'pet', 'status']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['employee'] = UserCustom.objects.filter(is_staff=True).first()
        cleaned_data['date'] = date.today()
        cleaned_data['status'] = Event.objects.filter(name='Pending').first()
        return cleaned_data
