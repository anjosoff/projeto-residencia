from django.urls import path
from . import views

urlpatterns=[ 

    path('', views.IndexEquipe, name='index_equipe')

]