from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
	return render(request, 'shopping/home.html')

def New_User(request):
	if request.method == "POST":  
		form = UserCreationForm(request.POST)
		if form.is_valid():

			form.save()
			return render(request, 'shopping/home.html', )
	else:
		form = UserCreationForm()
	return render(request,'shopping/New_User.html', {'form':form})

def Login(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return render(request, 'shopping/home.html')
	else:
		form = AuthenticationForm()
	return render(request, 'shopping/login.html', {'form':form})

def Logout(request):
	if request.method == 'POST':
		logout(request)
		return render(request, 'shopping/home.html')


'''
def Account(request):
	user = 
	return render(request, 'shopping/account.html', {'user':user})
'''

@login_required(login_url="/shopping/Login/")
def SpecialOffers(request):
	return render(request, 'shopping/specialoffers.html')


'''
def Login(request):
    if request.method == 'POST':
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
	    return render(request,'shopping/home.html')

	else:
		return render(request, 'shopping/login.html')
'''

'''
def User_Info(request):
	users = Customer.objects.all()
	return render(request, 'login.html', {'users': users})
'''

# Create your views here.
