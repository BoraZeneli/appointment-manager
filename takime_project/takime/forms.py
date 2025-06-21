from django import forms
from .models import Appointment, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'date', 'start_time', 'end_time', 'comment']
        widgets = {
    'client': forms.Select(attrs={'class': 'form-select'}),
    'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
    'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
    'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
}
        
