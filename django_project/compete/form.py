from django import forms
from .models import Compete

class CreateCompeteForm(forms.ModelForm):
    class Meta:
         model = Compete 
         exclude = ('user','company','job')
         


class UpdateCompeteForm(forms.ModelForm):
    class Meta:
         model = Compete 
         exclude = ('user','company','job')
         