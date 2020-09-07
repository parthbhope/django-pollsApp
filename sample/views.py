from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(reference):
	return render(reference , 'sample/home.html') 
	# returning template ,reference is the request object , the 2nd param is the path of the template inside the templates folder

def about(reference):
	return HttpResponse('<h1>About Us page</h1>')