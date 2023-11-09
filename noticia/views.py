from re import S
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Noticia

# Create your views here.
class NoticiaIndex(ListView):
    model=Noticia
    template_name='noticia/index.html'
    context_object_name='posts'
    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.order_by('-id').filter(publicado=True)
        return qs