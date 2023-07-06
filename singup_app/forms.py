from django import forms
from .models import User

class data(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]