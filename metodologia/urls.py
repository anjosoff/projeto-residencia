from django.urls import path 
from . import  views

urlpatterns=[
    path('', views.metodologia,name='index_metodologia'),
]