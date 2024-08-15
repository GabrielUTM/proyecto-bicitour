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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['id_inscripcion'].queryset = Inscripcion.objects.all()
        self.fields['id_inscripcion'].label_from_instance = lambda obj: f"{obj.usuario_nombre}"

