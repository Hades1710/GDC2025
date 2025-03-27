from django import forms
from django.contrib.auth.models import User
from . import models


class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientForm(forms.ModelForm):
    
    class Meta:
        model=models.Patient
        fields=['age','address','mobile','profile_pic','introduction','education','annual_income','student_background']
        widgets = {
            'student_background': forms.RadioSelect(attrs={'class': 'form-check-input'})
        }
