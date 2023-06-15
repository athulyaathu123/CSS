from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class Login(forms.Form):
#     username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter Password","class":"form-control"}))
#     password=forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}))
    
    
    
    

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    address=forms.CharField(max_length=100)
    
    
class Managerform(forms.Form):
    FIRST_NAME=forms.CharField(max_length=100)
    SECOND_NAME=forms.CharField(max_length=100)
    DOB=forms.DateField()
    PHONE=forms.IntegerField()
    EMAIL=forms.EmailField()
    QUALIFICATION=forms.CharField(max_length=100)
    
    
class Regform(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        
        
class Logform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)