# Generated by Django 3.2.6 on 2022-06-15 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='levelofinfo',
            name='code',
            field=models.CharField(default='d', max_length=5, verbose_name='NDI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelinfostage',
            name='code',
            field=models.CharField(default='d', max_length=5, verbose_name='EAIM'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='typeofinfo',
            name='code',
            field=models.CharField(default='d', max_length=5, verbose_name='TDI'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='levelofinfo',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nivel de información'),
        ),
        migrations.AlterField(
            model_name='modelinfostage',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Estado de avance'),
        ),
        migrations.AlterField(
            model_name='typeofinfo',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Tipo de información'),
        ),
    ]
