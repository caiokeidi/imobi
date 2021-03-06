# Generated by Django 3.1.5 on 2021-01-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_auto_20210130_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imoveis',
            name='valor_aluguel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='valor_condominio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='valor_iptu',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='valor_venda',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
