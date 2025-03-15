from django.db import models
 
class Movies(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    price = models.IntegerField()
    image = models.FileField(upload_to='media',blank=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    password = models.CharField(max_length=100)

class Booking(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    MovieId = models.ForeignKey(Movies,on_delete=models.CASCADE)
    sheet = models.CharField(max_length=100)
