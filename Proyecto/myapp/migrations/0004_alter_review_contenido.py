# Generated by Django 5.1.4 on 2024-12-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_review_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='contenido',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
