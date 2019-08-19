from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
def home(request):
	return render(request, 'home.html')

def New_User(request):

	if request.method == "POST":

		user = CustomerForm(request.POST)
		if user.is_valid():

			user.save()
		

	return render(request, 'thankyou.html')
def User_Login(request):
	return render(request, 'home.html')

# Create your views here.
