# Generated by Django 2.2.3 on 2022-07-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_cat',
            field=models.CharField(max_length=50, verbose_name='Nome da categoria'),
        ),
    ]
