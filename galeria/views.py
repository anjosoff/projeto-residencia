import imp
from turtle import update
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from comentarios.models import Comentario
from .models import Galeria
from django.db.models import Q,Count,Case,When
from comentarios.forms import FormComentario
from django.contrib import messages
class GaleriaIndex(ListView):
    model=Galeria
    template_name='galeria/index.html'
    context_object_name='posts'
    def get_queryset(self):
        qs=super().get_queryset()
        qs=qs.order_by('-id').filter(publicado=True)
        qs=qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs
class GaleriaDetalhes(UpdateView):
    model=Galeria
    template_name='galeria/galeria_detalhes.html'
    form_class=FormComentario
    context_object_name='post'
    def get_context_data(self, **kwargs):
        contexto=super().get_context_data(**kwargs)
        post=self.get_object()
        comentarios=Comentario.objects.filter(
        publicado_comentario=True,
        galeria_comentario=post.id)
        contexto['comentarios']=comentarios
        return contexto
    def form_valid(self,form):
        post=self.get_object()
        comentarios=Comentario(**form.cleaned_data)
        comentarios.galeria_comentario=post
        if self.request.user.is_authenticated:
            comentarios.usuario_comentario=self.request.user
        comentarios.save()
        messages.success(self.request,'O seu comentário foi enviado para análise, em breve estará disponível para visualização aqui na galeria!')
        return redirect('galeria_detalhes',pk=post.id)