from django.shortcuts import render
from django.http import HttpResponse
from .helperfiles.recommendation import critics,list_of_movies
# Create your views here.

def home(request):
	lsofmovie=list_of_movies()
	context=critics;
	return render(request,'index.html',{'context':context,
		'lsofmovie':lsofmovie})