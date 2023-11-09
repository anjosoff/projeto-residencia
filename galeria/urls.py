from django.urls import path
from . import views

urlpatterns=[ 

    path('',views.GaleriaIndex.as_view(), name='index_galeria'),
    path('<int:pk>',views.GaleriaDetalhes.as_view(), name='galeria_detalhes'),


]