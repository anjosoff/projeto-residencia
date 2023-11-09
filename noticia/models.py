from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categoria
from django.utils import timezone
# Create your models here.
class Noticia(models.Model):
    titulo=models.CharField(max_length=255,verbose_name='Titulo')
    link=models.CharField(max_length=255,verbose_name='Link da Noticia')
    autor=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
    data =models.DateTimeField(default=timezone.now,verbose_name='Data')
    descricao=models.TextField(verbose_name='Descrição')
    categoria =models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,verbose_name='Categoria')
    imagem_noticia=models.ImageField(upload_to='noticias/%Y/%m/%d',blank=True, null=False,verbose_name='Imagem da noticia')
    publicado=models.BooleanField(default=False,verbose_name='Publicado')
    def __str__(self) :
        return self.titulo
