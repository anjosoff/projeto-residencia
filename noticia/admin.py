from django.contrib import admin
from noticia.models import Noticia
# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):
    list_display=('id',
                'titulo',
                'autor',
                'data',
                'publicado',)
    list_editable=('publicado',)
    list_display_links=('id','titulo',)

admin.site.register(Noticia,NoticiaAdmin)