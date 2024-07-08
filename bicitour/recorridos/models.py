from django.db import models

# Create your models here.
class Recorridos(models.Model): #Define la estructura de nuestra tabla
    fecha = models.DateTimeField(auto_now_add=True) #Texto largo
    hora = models.TimeField(auto_now_add=True)
    estado = models.TextField(max_length=15)
    ciudad = models.TextField() #Fecha y tiempo
    km_recorrido = models.FloatField()
    tiempo_estimado = models.TimeField()
    punto_inicio = models.TextField()
    costo = models.IntegerField()
    foto_zona_visitar = models.TextField()
    activo = models.BooleanField(True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["-created"]

    def __str__(self):
        return self.punto_inicio
        