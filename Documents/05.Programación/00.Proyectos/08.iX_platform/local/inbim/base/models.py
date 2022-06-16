from django.db import models

class TypeOfInfo(models.Model):
    # Modelo de Tipos de información
    name = models.CharField(
        max_length=255,
        verbose_name="Tipo de información"
    )
    code = models.CharField(
        max_length=5,
        verbose_name='TDI'
    )
    description = models.TextField(
        verbose_name="Descripción"
    )

    # Relación a Atributos y Propiedades

class LevelOfInfo(models.Model):
    # Modelo de Niveles de información
    name = models.CharField(
        max_length=255,
        verbose_name="Nivel de información"
    )
    code = models.CharField(
        max_length=5,
        verbose_name='NDI'
    )
    description = models.TextField(
        verbose_name="Descripción"
    )

    # Relación a Atributos y Propiedades

class ModelInfoStage(models.Model):
    # Modelo de Estados de Avance de la Información de los Modelos
    name = models.CharField(
        max_length=255,
        verbose_name="Estado de avance"
    )
    code = models.CharField(
        max_length=5,
        verbose_name='EAIM'
    )
    # Relación a los modelos disponibles para cada EAIM

    # Relación a las propiedades y atributos

class BimUse(models.Model):
    # Modelo de Usos BIM
    name = models.CharField(
        max_length=255,
        verbose_name="Uso BIM"
    )
    description = models.TextField(
        verbose_name="Descripción"
    )
    types_of_info = models.ManyToManyField(
        TypeOfInfo,
        related_name='usos_bim'
        )
    # Relación a recursos sugeridos

    # Relación a capacidades BIM

    # Relació  a Experiencia o conocimiento previo


class IfcEntity(models.Model):
    # Modelo de Entidades IFC
    name = models.CharField(
        max_length=255,
        verbose_name="Entidad Ifc"
    )
    translation = models.CharField(
        max_length=255,
        verbose_name="Traducción"
    )
    parent_entity = models.CharField(
        max_length=255,
        verbose_name="Entidad superior",
        blank=True, 
        null=True
    )
    # Tipos Predefinidos (Relación o atributo)

    # Relación a modelos BIM

    # Relación a Atributos y Propiedades IFC 

class IfcPropSet(models.Model):
    # Modelo de grupo de propiedades IFC (Pset y Qto)
    name = models.CharField(
        max_length=255,
        verbose_name="Conjunto de propiedades"
    )

    # Relacuón a propiedades

class IfcAttribute(models.Model):
    # Modelo de Atributos IFC
    name = models.CharField(
        max_length = 255,
        verbose_name="Atributo"
    )
    data_type = models.CharField(
        max_length = 255,
        verbose_name="Tipo de dato"
    )
    translation = models.CharField(
        max_length=255,
        verbose_name="Traducción"
    )
    type_of_info = models.ForeignKey(
        TypeOfInfo,
        verbose_name='atributos',
        on_delete=models.DO_NOTHING
        )
    level_of_info = models.ForeignKey(
        LevelOfInfo,
        related_name='atributos_de_ndi',
        on_delete= models.DO_NOTHING
    )
    ifc_entities = models.ManyToManyField(
        IfcEntity,
        related_name='atributos_de_entidad'
    )


class IfcProperty(models.Model):
    # Modelo de Propiedaes IFC
    name = models.CharField(
        max_length=255,
        verbose_name="Propiedad"
    )
    data_type = models.CharField(
        max_length=255,
        verbose_name="Tipo de dato"
    )
    translation = models.CharField(
        max_length=255,
        verbose_name="Traducción"
    )
    type_of_info = models.ForeignKey(
        TypeOfInfo,
        verbose_name='propiedades',
        on_delete=models.DO_NOTHING
        )
    level_of_info = models.ForeignKey(
        LevelOfInfo,
        related_name='propiedades_de_ndi',
        on_delete= models.DO_NOTHING
    )
    ifc_entities = models.ManyToManyField(
        IfcEntity,
        related_name='propiedades_de_entidad'
    )
    property_sets = models.ManyToManyField(
        IfcPropSet,
        related_name='propiedades_pset'
    )

class BimModel(models.Model):
    # Modelo de Tipo de Modelo BIM
    name = models.CharField(
        max_length=255,
        verbose_name="Tipo de modelo"
    )
    ifc_entities = models.ManyToManyField(
        IfcEntity,
        related_name='entidades_modelo'
    )
    bim_uses = models.ManyToManyField(
        BimUse,
        related_name='usos_bim_modelo'
    )
    model_info_stage = models.ManyToManyField(
        ModelInfoStage,
        related_name='eaim_modelo'
    )