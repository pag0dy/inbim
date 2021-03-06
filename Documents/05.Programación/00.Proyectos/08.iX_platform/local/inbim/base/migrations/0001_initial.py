# Generated by Django 3.2.6 on 2022-06-15 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IfcEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Entidad Ifc')),
                ('translation', models.CharField(max_length=255, verbose_name='Traducción')),
                ('parent_entity', models.CharField(blank=True, max_length=255, null=True, verbose_name='Entidad superior')),
            ],
        ),
        migrations.CreateModel(
            name='IfcPropSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Conjunto de propiedades')),
            ],
        ),
        migrations.CreateModel(
            name='LevelOfInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='Nivel de información')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='ModelInfoStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='EAIM')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='Tipo de información')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='IfcProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Propiedad')),
                ('data_type', models.CharField(max_length=255, verbose_name='Tipo de dato')),
                ('translation', models.CharField(max_length=255, verbose_name='Traducción')),
                ('ifc_entities', models.ManyToManyField(related_name='propiedades_de_entidad', to='base.IfcEntity')),
                ('level_of_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='propiedades_de_ndi', to='base.levelofinfo')),
                ('property_sets', models.ManyToManyField(related_name='propiedades_pset', to='base.IfcPropSet')),
                ('type_of_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.typeofinfo', verbose_name='propiedades')),
            ],
        ),
        migrations.CreateModel(
            name='IfcAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Atributo')),
                ('data_type', models.CharField(max_length=255, verbose_name='Tipo de dato')),
                ('translation', models.CharField(max_length=255, verbose_name='Traducción')),
                ('ifc_entities', models.ManyToManyField(related_name='atributos_de_entidad', to='base.IfcEntity')),
                ('level_of_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='atributos_de_ndi', to='base.levelofinfo')),
                ('type_of_info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.typeofinfo', verbose_name='atributos')),
            ],
        ),
        migrations.CreateModel(
            name='BimUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Uso BIM')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('types_of_info', models.ManyToManyField(related_name='usos_bim', to='base.TypeOfInfo')),
            ],
        ),
        migrations.CreateModel(
            name='BimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tipo de modelo')),
                ('bim_uses', models.ManyToManyField(related_name='usos_bim_modelo', to='base.BimUse')),
                ('ifc_entities', models.ManyToManyField(related_name='entidades_modelo', to='base.IfcEntity')),
                ('model_info_stage', models.ManyToManyField(related_name='eaim_modelo', to='base.ModelInfoStage')),
            ],
        ),
    ]
