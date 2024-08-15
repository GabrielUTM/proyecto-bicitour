from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.
# Define la estructura de la tabla 'Recorridos' en la base de datos
class Recorridos(models.Model):
    id_recorrido = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=70)
    ciudad = models.CharField(max_length=70)
    km_recorrido = models.FloatField(verbose_name="Kilómetros")
    tiempo_estimado = models.TimeField(verbose_name="Tiempo estimado en horas")
    punto_inicio = models.TextField(max_length=200)
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Costo")
    foto_zona_visitar = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["created"]

    def __str__(self):
        return self.estado 


class Inscripcion(models.Model):
    text_validator = RegexValidator(
        regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
        message="Este campo solo puede contener letras y espacios."
        )
    id_inscripcion = models.AutoField(primary_key=True,)
    id_recorrido = models.ForeignKey(Recorridos, on_delete=models.CASCADE, verbose_name="Recorridos")
    usuario_nombre = models.CharField(max_length=60, verbose_name="Nombre:", validators=[text_validator])
    usuario_correo_electronico = models.EmailField(max_length=80,verbose_name="Correo electronico:", validators=[EmailValidator()], db_index=True)
    usuario_telefono = models.CharField(max_length=10,verbose_name="Telefono:", validators=[MinLengthValidator(10), MaxLengthValidator(10)], db_index=True)
    usuario_ciudad = models.CharField(max_length=60,verbose_name="Ciudad:", validators=[text_validator])
    usuario_estado = models.CharField(max_length=60,verbose_name="Estado:", validators=[text_validator])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"
        ordering = ["created"]

    def __str__(self):
        return self.usuario_nombre
    




class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_recorrido = models.ForeignKey(Recorridos, on_delete=models.CASCADE, verbose_name="Recorrido")
    id_inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, verbose_name="Inscripcion")
    comentario = models.TextField()
    calificacion = models.IntegerField(validators=[MaxLengthValidator(5), MinLengthValidator(1)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["created"]

    def __str__(self):
        return self.id_comentario