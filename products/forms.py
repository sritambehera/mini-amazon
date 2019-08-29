from django import forms
from .models import Products



class ProductsForm(forms.Form):

	class meta:
		model = Products
		fields = ('items')
		