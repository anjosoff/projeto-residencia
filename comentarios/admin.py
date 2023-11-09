from django.contrib import admin
from comentarios.models import Comentario
# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display=('id',
                'nome',
                'email',
                'data_comentario',
                'galeria_comentario',
                'publicado_comentario',)
    list_editable=('publicado_comentario',)
    list_display_links=('id','nome',)

admin.site.register(Comentario,ComentarioAdmin)