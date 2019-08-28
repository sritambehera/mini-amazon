from django.db import models
from django.forms import ModelForm
from django.conf import settings

class Products(models.Model):
	items = models.ImageField(upload_to = 'assets/')




# Create your models here.
