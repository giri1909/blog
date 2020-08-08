from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib import admin
from .views import Home
from .views import testappTest

from .views import Employees#Name

urlpatterns = [
   
    url(r'^home/',Home),  
    url(r'^employee/',Employees),  
    url(r'^testapptest/',testappTest),
    #url(r'^name/',Name),
]

