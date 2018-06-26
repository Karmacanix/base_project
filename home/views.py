from django.shortcuts import render
import requests

# Create your views here.
def home(request):	
	return render(request, 'home.html')


def who(request):	
	return render(request, 'who_are_we.html')


def what(request):	
	return render(request, 'what_do_we_do.html')


def help(request):	
	return render(request, 'help.html')