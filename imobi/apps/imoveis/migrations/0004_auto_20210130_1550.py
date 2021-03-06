# Generated by Django 3.1.5 on 2021-01-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_auto_20210130_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imoveis',
            name='andar',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='complemento',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='descricao',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='metro_proximo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='valor_aluguel',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='valor_venda',
            field=models.IntegerField(blank=True),
        ),
    ]
