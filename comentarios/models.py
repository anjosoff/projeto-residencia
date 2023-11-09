from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import User
from django.utils import timezone
from galeria.models import Galeria
# Create your models here.
class Comentario(models.Model):
    nome=models.CharField(max_length=150,verbose_name='Nome',null=False)
    email =models.EmailField(verbose_name='Email')
    comentario =models.TextField(default='',verbose_name='Comentario')
    galeria_comentario=models.ForeignKey(Galeria, on_delete=models.CASCADE,verbose_name='Comentario na galeria')
    usuario_comentario=models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='Usuario do Comentário',blank=True,null=True)
    data_comentario=models.DateTimeField(default=timezone.now,verbose_name='Data do comentário',null=False)
    publicado_comentario=models.BooleanField(default=False,verbose_name='Publicado')
    def __str__(self) :
        return self.nome