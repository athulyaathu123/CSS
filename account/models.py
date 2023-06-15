from django.db import models

# Create your models here.
class Manager(models.Model):
    FIRST_NAME=models.CharField(max_length=100)
    SECOND_NAME=models.CharField(max_length=100)
    DOB=models.DateField()
    PHONE=models.IntegerField()
    EMAIL=models.EmailField()
    QUALIFICATION=models.CharField(max_length=100)
    
    