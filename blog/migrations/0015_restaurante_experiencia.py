# Generated by Django 4.1.2 on 2022-12-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_restaurante_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='experiencia',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
