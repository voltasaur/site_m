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
from django.conf.urls import url
from django.urls import path
from hotel.views import site, test, hello_python, sum_two, ofice_hotel, proba

urlpatterns = [
    path('', site),
    url(r'^python/$', hello_python),
	url(r'^new/$', test),
	url(r'^ofice_hotel/$', ofice_hotel),
    url(r'^proba/$', proba),
	url(r'^sum/(\d+)/(\d+)/$', sum_two),
    path('admin/', admin.site.urls),
]




