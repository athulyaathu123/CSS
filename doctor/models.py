from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=500)
    phone=models.IntegerField()
    
    
class Doctor(models.Model):
    first_name=models.CharField(max_length=100,verbose_name="Enter your First Name ")
    last_name=models.CharField(max_length=100,verbose_name="Enter your Last Name ")
    email=models.EmailField(verbose_name="Enter your Email ")
    qualification=models.CharField(max_length=100,verbose_name="Enter your Qualification ")
    dept=models.CharField(max_length=100,verbose_name="Enter your Department ")
    profile_pic=models.ImageField(upload_to="doc_profile",null=True)