# Generated by Django 4.2.2 on 2023-06-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0010_alter_valores_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencia',
            name='nombreProyecto',
            field=models.TextField(),
        ),
    ]