from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
	
	name = models.CharField(max_length=50)
	email= models.CharField(max_length=50)
	password= models.CharField(max_length=10)


# Create your models here
