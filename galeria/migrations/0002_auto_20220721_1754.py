# Generated by Django 2.2.3 on 2022-07-21 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='conteudo',
            field=models.TextField(verbose_name='Conteudo'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='excerto',
            field=models.TextField(verbose_name='Excerto'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='galeria_img/Y%/%m/%d', verbose_name='Imagem da galeria'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='publicado',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
    ]