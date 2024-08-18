from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Comentario, Recorridos, Inscripcion

class ComentarioResource(resources.ModelResource):
    ciudad = fields.Field(
        column_name='ciudad',
        attribute='id_recorrido',
        widget=ForeignKeyWidget(Recorridos, 'ciudad')
    )

    usuario_nombre = fields.Field(
        column_name='usuario_nombre',
        attribute='id_inscripcion',
        widget=ForeignKeyWidget(Inscripcion, 'usuario_nombre')
    )

    class Meta:
        model = Comentario
        fields = ('id_comentario', 'ciudad', 'usuario_nombre', 'comentario', 'calificacion', 'created', 'updated')
        export_order = ('id_comentario', 'ciudad', 'usuario_nombre', 'comentario', 'calificacion', 'created', 'updated')
