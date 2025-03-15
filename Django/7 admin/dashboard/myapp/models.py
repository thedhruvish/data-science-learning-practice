from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    contact = models.IntegerField()
    role = models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    image = models.FileField(upload_to='media',default='')

class Branch(models.Model):
    b_name = models.CharField(max_length=255,unique=True)

class Course(models.Model):
    c_name = models.CharField(max_length=255,unique=True)

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    contact = models.IntegerField()
    course=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    detail=models.CharField(max_length=100)
    inquiryby=models.CharField(max_length=100)
    total_fee=models.IntegerField()
    date=models.DateTimeField()
    status=models.CharField(max_length=100)