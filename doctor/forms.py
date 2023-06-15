from typing import Any, Dict
from django import forms
from .models import Doctor




class AdmitForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter Name","class":"form-control"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Age","class":"form-control"}))
    disease=forms.CharField(max_length=100,widget=forms.Textarea(attrs={"placeholder":"Enter Disease report","class":"form-control"}))
    date=forms.DateField(widget=forms.DateInput(attrs={"placeholder":"Enter Date","class":"form-control"}))
    admission_no=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter ad:no","class":"form-control"}))
    otp=forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"placeholder":"Enter otp","class":"form-control"}))
    
    
    
    def clean(self):
        cleaned_data=super().clean()
        ag=cleaned_data.get("age")
        an=cleaned_data.get("admission_no")
        if ag<13:
            self.add_error("age","Age must be greater than 13")
        if an<=0:
            self.add_error("admission_no","Admission no must be greater than 0")
            
            
class Calculator(forms.Form):
    value=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter the value :","class":"form-control"}))
    
    def clean(self):
        cleaned_data= super().clean()
        
        
class Patientform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    address=forms.CharField(max_length=100)
    phone=forms.IntegerField()
    
    
    
class Docterform(forms.ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "qualification":forms.TextInput(attrs={"class":"form-control"}),
            "dept":forms.TextInput(attrs={"class":"form-control"})
        }