# forms.py
from django import forms
from .models import Comentario, Inscripcion

class RegistroParticipantesForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ["id_recorrido", "usuario_nombre", "usuario_correo_electronico", "usuario_telefono", "usuario_ciudad", "usuario_estado"]


#Formulario para obtener el nombre de la persona inscrita
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['id_recorrido', 'id_inscripcion', 'comentario', 'calificacion']

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['calificacion'].widget = forms.RadioSelect(choices=[(i, f'{i} estrellas') for i in range(1, 6)])
