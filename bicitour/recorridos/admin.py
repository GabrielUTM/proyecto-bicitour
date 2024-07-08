from django.contrib import admin
from .models import Recorridos
# Register your models here.
class AdministrarRecorrido(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Recorridos, AdministrarRecorrido)