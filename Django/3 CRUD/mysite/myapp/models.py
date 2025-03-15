from django.db import models


# Create your models here.
class user_details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    number = models.IntegerField()
    gender = models.CharField(max_length=1000) 
    hobby = models.CharField(max_length=1000) 
    city = models.CharField(max_length=1000) 

    image = models.ImageField(upload_to='media/' ,blank=True,null=True )



