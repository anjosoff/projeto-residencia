
from site import execusercustomize
from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categoria
from django.utils import timezone

class Galeria(models.Model):
    titulo=models.CharField(max_length=255,verbose_name='Titulo')
    autor=models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='Autor')
    data =models.DateTimeField(default=timezone.now,verbose_name='Nome')
    conteudo=models.TextField(verbose_name='Conteudo')
    excerto =models.TextField(verbose_name='Excerto')
    categoria =models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,verbose_name='Categoria')
    imagem_galeria=models.ImageField(upload_to='galerias/%Y/%m/%d',blank=True, null=False,verbose_name='Imagem da galeria')
    publicado=models.BooleanField(default=False,verbose_name='Publicado')
    def __str__(self) :
        return self.titulo