from .models import IfcDoc

def filtro_archivo(id):
    activo = IfcDoc.objects.filter(id=id)
    if activo:
        modelo_activo = activo[0]
        return modelo_activo
    else:
        mensaje = 'No se encontrĂ³ el modelo'
        print(mensaje)
        return mensaje