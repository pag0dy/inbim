from django.contrib import admin
from .models import TypeOfInfo, LevelOfInfo, ModelInfoStage, BimUse, IfcEntity, IfcPropSet, IfcAttribute, IfcProperty, BimModel

class TypeOfInfoAdmin(admin.ModelAdmin):
    fields = ['name','code', 'description']
    list_display = ['name', 'code', 'description']

class LevelOfInfoAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'description']
    list_display = ['name', 'code', 'description']

class ModelInfoStageAdmin(admin.ModelAdmin):
    fields = ['name', 'code']
    list_display = ['name', 'code']

class BimUseAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    list_display = ['name', 'description']

class IfcEntityAdmin(admin.ModelAdmin):
    fields = ['name', 'translation', 'parent_entity']
    list_display = ['name', 'translation', 'parent_entity']

class IfcPropSetAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']

class IfcAttributeAdmin(admin.ModelAdmin):
    fields = ['name', 'data_type', 'translation', 'type_of_info', 'level_of_info']
    list_display = ['name', 'data_type', 'translation', 'type_of_info', 'level_of_info']

class IfcPropertyAdmin(admin.ModelAdmin):
    fields = ['name', 'data_type', 'translation', 'type_of_info', 'level_of_info']
    list_display = ['name', 'data_type', 'translation', 'type_of_info', 'level_of_info']

class BimModelAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']

admin.site.register(TypeOfInfo, TypeOfInfoAdmin)
admin.site.register(LevelOfInfo, LevelOfInfoAdmin)
admin.site.register(ModelInfoStage, ModelInfoStageAdmin)
admin.site.register(BimUse, BimUseAdmin)
admin.site.register(IfcEntity, IfcEntityAdmin)
admin.site.register(IfcPropSet, IfcPropSetAdmin)
admin.site.register(IfcAttribute, IfcAttributeAdmin)
admin.site.register(IfcProperty, IfcPropertyAdmin)
admin.site.register(BimModel, BimModelAdmin)
