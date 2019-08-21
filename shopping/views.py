from django.shortcuts import redirect
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
	users = Customer.objects.all()
		

	return render(request, 'thankyou.html', {'users': users})

def Login(request):
	return render(request, 'login.html')









	'''
def User_Info(request):
	users = Customer.objects.all()
	return render(request, 'login.html', {'users': users})
'''

# Create your views here.
