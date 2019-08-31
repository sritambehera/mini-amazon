from django.db import models
from django.contrib.auth.models import User



class UserCart(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	cart_item = models.ForeignKey('products.Products', null = True, on_delete = models.CASCADE)
	


		



# Create your models here
