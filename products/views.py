from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from .forms import ProductsForm
from django.contrib.auth.decorators import login_required

def Category(request):
	return render(request, 'products/category.html')

#	@login_required(login_url ='/shopping/Login.html')
def Sell(request):
	if request.method == "POST":
		form = ProductsForm(request.POST, request.FILES,)
		if form.is_valid():
			form.save()
		return render(request, 'shopping/home.html')
	else:
		form = ProductsForm()	
	return render(request, 'products/sell.html', {'form':form})
       


		
	
	

# Create your views here.
