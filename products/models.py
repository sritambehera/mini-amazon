from django.db import models
from django.forms import ModelForm
from django.conf import settings

class Products(models.Model):
    items = models.FileField(upload_to = 'assets')


# Create your models here.
