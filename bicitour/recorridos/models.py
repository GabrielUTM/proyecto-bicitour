from django.db import models

# Create your models here.
# Define la estructura de la tabla 'Recorridos' en la base de datos
class Recorridos(models.Model):
    id_recorrido = models.CharField(max_length=255, primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    estado = models.TextField(max_length=15)
    ciudad = models.TextField()
    km_recorrido = models.FloatField()
    tiempo_estimado = models.TimeField()
    punto_inicio = models.TextField()
    costo = models.IntegerField()
    foto_zona_visitar = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["created"]

    def __str__(self):
        return self.id_recorrido


class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    id_recorrido = models.ForeignKey('Recorridos', on_delete=models.CASCADE)
    usuario_nombre = models.CharField(max_length=255, verbose_name="Nombre:")
    usuario_correo_electronico = models.CharField(max_length=255,verbose_name="Correo electronico:")
    usuario_telefono = models.CharField(max_length=20,verbose_name="Telefono:")
    usuario_ciudad = models.CharField(max_length=255,verbose_name="Ciudad:")
    usuario_estado = models.CharField(max_length=255,verbose_name="Estado")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"
        ordering = ["created"]

    def __str__(self):
        return str(self.id_inscripcion)


class Comentario(models.Model):
    id_comentario = models.CharField(max_length=255)
    id_recorrido = models.ForeignKey('Recorridos', on_delete=models.CASCADE)
    id_inscripcion = models.ForeignKey('Inscripcion', on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["created"]

    def __str__(self):
        return self.id_comentario