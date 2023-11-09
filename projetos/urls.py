from django.urls import path 
from . import views

urlpatterns=[ 
    path('', views.projetos, name='index_projetos'),
    path('desenvolvimento', views.dev, name='index_dev'),
    path('infraestrutura', views.infra, name='index_infra'),
    path('business-inteligence', views.business, name='index_bi'),
]