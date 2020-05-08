from django.db import models

# Create your models here.

class Userinfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    mobile = models.BigIntegerField()
    password  = models.CharField(max_length=32)

