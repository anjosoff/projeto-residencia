# Generated by Django 4.0.6 on 2022-08-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_auto_20220725_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]