from django.db import models
from django.contrib.auth.models import User



class UserCart(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE) 
	cart_item = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.cart_item

# Create your models here
