from django.db import models
class Customer(models.Model):
	
	name = models.CharField(max_length=50)
	email= models.CharField(max_length=50)
	password= models.CharField(max_length=10)


# Create your models here
