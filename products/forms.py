from django import forms
from .models import Products



class ProductsForm(forms.ModelForm):

	class meta:
		model = Products
		fields = ('items')
		