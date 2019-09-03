from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Products
from shopping.models import UserCart

def home(request):
	data = Products.objects.all()
	return render(request, 'shopping/home.html', {'data':data, 'media_url':settings.MEDIA_URL})

def New_User(request):
	if request.method == "POST":  
		form = UserCreationForm(data = request.POST)
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
			return redirect('/shopping/')
	else:
		form = AuthenticationForm()
	return render(request, 'shopping/login.html', {'form':form})

def Logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/shopping/')

def Cart(request):
	user1 = None
	if request.user.is_authenticated:
		'''
		NOTE: I was doing a silly mf silly mistake that i passed  user name manually as (for filtering user_cart_items)

		customer_name = 'sritam'
		but after that i used to pass: customer_name ='request.user' (notice that request.user is being passed in a string format which is absolutely not understandable by the code compiler)
        (I searched this in google, stackoverflow , django documentation etc.)
		IT TOOK ALMOST 2 DAYS FOR DEBUGGING THIS ERROR ( as i am new to django 🙂)
		Whatever... great learning!
		No matter how samll the error is. It is always going to be a error in your code 


		'''
		var = UserCart.objects.filter(customer__username = request.user)    
		return render(request, 'shopping/cart.html', {'var':var})


'''
def Account(request):
	user = 
	return render(request, 'shopping/account.html', {'user':user})
'''
'''
def Cart(request):

	if request.method == "POST":
		form = UserCart(request.POST)
		form.save()
		return render(request, 'shopping/cart.html')
	else:
		form = UserCart()
	return redirect( '/shopping/',{'form':form})
'''

@login_required(login_url="/shopping/Login/")
def SpecialOffers(request):
	return render(request, 'shopping/specialoffers.html')


@login_required(login_url="/shopping/Login/")
def Change_Password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return render('/shopping/')

	else:
		form = PasswordChangeForm(request.user)

	
	return render(request, 'shopping/changepassword.html', {'form':form})


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
