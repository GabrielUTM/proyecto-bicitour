from django.db import models

# Create your models here.
# Define la estructura de la tabla 'Recorridos' en la base de datos
class Recorridos(models.Model): 
    fecha = models.DateTimeField(auto_now_add=True) 
    hora = models.TimeField(auto_now_add=True)
    estado = models.TextField(max_length=15)
    ciudad = models.TextField() 
    km_recorrido = models.FloatField()
    tiempo_estimado = models.TimeField()
    punto_inicio = models.TextField()
    costo = models.IntegerField()
    foto_zona_visitar = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    activo = models.BooleanField(True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["-created"]

    def __str__(self):
        return self.punto_inicio
        