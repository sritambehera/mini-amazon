from django.shortcuts import render, redirect
from django.http import HttpResponse

def base(request):
	return render(request, 'base.html')