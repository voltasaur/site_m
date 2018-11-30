"""st_mag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

def site(request):
    return render(request,"index.html")

def hello_python(request):
    return render(request,"python.html")

def hello_python_old(request, a, b):
    s = int(a) + int(b) 
    print ('----------------------'+ str(s)+'----------------------')
    return HttpResponse("<h1> ONE SITE PYTHON </h1>" + str(s) )

urlpatterns = [
    path('', site),
    url(r'^python/$', hello_python),
    path('admin/', admin.site.urls),
]




