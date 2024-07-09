from django.contrib import admin
from .models import Recorridos
from .models import Inscripcion
from .models import Comentario
from .forms import ComentarioForm
# Register your models here.




class AdministrarRecorrido(admin.ModelAdmin):
    list_display = ('id_recorrido', 'fecha', 'hora', 'estado', 'ciudad', 'km_recorrido', 'tiempo_estimado', 'punto_inicio', 'costo', 'activo', 'created', 'updated')
    search_fields = ('id_recorrido', 'estado', 'ciudad')
    list_filter = ('estado', 'ciudad', 'activo')
    date_hierarchy = 'fecha'
    readonly_fields = ('created', 'updated')

admin.site.register(Recorridos, AdministrarRecorrido)

class AdministrarComentarios(admin.ModelAdmin):
    form = ComentarioForm
    list_display = ('id_comentario', 'id_recorrido', 'get_usuario_nombre', 'comentario', 'calificacion', 'created')
    search_fields = ('id_comentario', 'comentario')
    list_filter = ('calificacion', 'id_recorrido')
    readonly_fields = ('id_comentario','created')

    #Método personalizado para obtener el nombre de usuario desde la inscripción relacionada.
    def get_usuario_nombre(self, obj):
        return obj.id_inscripcion.usuario_nombre
    get_usuario_nombre.short_description = 'Usuario Nombre'

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarInscripcion(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'id_recorrido', 'usuario_nombre', 'usuario_correo_electronico', 'usuario_telefono', 'usuario_ciudad', 'usuario_estado')
    search_fields = ('usuario_nombre', 'usuario_correo_electronico')
    list_filter = ('usuario_ciudad', 'usuario_estado')
admin.site.register(Inscripcion, AdministrarInscripcion)