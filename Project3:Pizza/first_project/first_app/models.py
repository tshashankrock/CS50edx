from django.db import models
from django import forms
# Create your models here.
class Users(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class category(models.Model):
        catid = models.IntegerField()
        catname = models.CharField(max_length=50)

        def __str__(self):
            return self.catname

class pizzaselection(models.Model):
        pid = models.IntegerField()
        catid = models.ForeignKey(category,on_delete = models.CASCADE)
        pname = models.CharField(max_length=50)
        psize = models.CharField(max_length=100)
        pprice = models.FloatField()
        tname = models.CharField(max_length=50) # topping name

        def __str__(self):
            return self.pid
