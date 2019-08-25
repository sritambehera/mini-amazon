from django.shortcuts import render
from django.http import HttpResponse

def Category(request):
	return render(request, 'products/category.html')
	

# Create your views here.
