# Generated by Django 2.2.3 on 2022-07-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_auto_20220726_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('link', models.CharField(max_length=255, verbose_name='Link do video')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
            ],
        ),
    ]
