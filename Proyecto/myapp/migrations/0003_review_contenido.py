# Generated by Django 5.1.4 on 2024-12-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_libro_autor_alter_libro_genero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='contenido',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
