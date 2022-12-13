from django.contrib import admin
from django.urls import path
from .import views


urlpatterns=[

    path('Sighup',views.sighup,name='sighup'),
    path('Login',views.login,name='login'),
    
]
