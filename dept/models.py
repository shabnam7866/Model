# from django.contrib.auth.models import User
from django.db import models

# Create your models here.

    
class Department(models.Model):
    # D_id=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    
    def __str__(self):
     return self.dept_name

class Adhar(models.Model):
    Adhar_number=models.IntegerField() 

    
    def __str__(self):
       return str(self.Adhar_number)
 
class Employee(models.Model):
    adhar=models.OneToOneField(Adhar, on_delete=models.CASCADE, default=False)
    emp_name=models.CharField(max_length=50)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    email=models.EmailField(max_length=50)


    def __str__(self):
     return self.emp_name

class Product(models.Model):
    emp=models.ManyToManyField(Employee)
    name = models.CharField(max_length=200)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name

         