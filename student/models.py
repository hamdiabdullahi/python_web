from django.db import models


# Create your models here.

class Student(models.Model):

    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age =models.PositiveSmallIntegerField(max_length=3)
    dateofbirth=models.DateField(max_length=10)





    
