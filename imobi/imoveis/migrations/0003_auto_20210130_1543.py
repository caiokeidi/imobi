# Generated by Django 3.1.5 on 2021-01-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0002_imagens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imoveis',
            name='cliente',
            field=models.CharField(max_length=50),
        ),
    ]
