from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from hotel.models import Ofice
# Create your views here.

def site(request):
	return render(request,"index.html")

def ofice_hotel(request):
	ofice = Ofice.objects.all()
	return render(request,"ofice_hotel.html", {"ofice_list": ofice} )

def proba(request):
	return render(request,"proba.html")

def test(request):	
	#print(dir(request))
	#print(request.method)
	#print(request.content_type)
	#print(request.GET)
	#print(request.POST)
	#print(request.POST['some'])
	responce = render(request,"new.html")
	#print(dir(responce))
	print('Content-Type: ' + responce['Content-Type'])
	responce['Age'] = 2000
	return responce

def hello_python(request):
	#print(dir(request))
	#print(request.method)
	#print(request.content_type)
	print(request.GET)
	print(request.POST)
	#print(request.META)
	return render(request,"python.html")

def sum_two(request, a, b):
    s = int(a) + int(b) 
    print ('----------------------'+ str(s)+'----------------------')
    return HttpResponse("<h1> ONE SITE PYTHON {} </h1>".format(s) )

