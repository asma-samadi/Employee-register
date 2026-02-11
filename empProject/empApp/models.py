from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=50)

class Employee(models.Model):
    fullName=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    email=models.EmailField()
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
