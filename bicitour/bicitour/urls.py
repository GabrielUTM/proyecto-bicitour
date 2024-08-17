"""
URL configuration for bicitour project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views
from recorridos import views as views_recorridos
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.principal, name="Principal"),
    path('Recorridos-Proximos/', views_recorridos.recorridosProximos, name="RecorridosProximos"),
    path('Recorridos-Finalizados/', views_recorridos.recorridosFinalizados, name="RecorridosFinalizados"),
    path('detalle/<int:id>', views_recorridos.detalle_recorrido, name="Detalle"),
    path('pre-registro/<int:id>', views_recorridos.pre_registro,name="Pre-registro"),
    path('Registrar-Participante/<int:id>', views_recorridos.registrarParticipante,name="RegistrarParticipante"),
    path('Mostrar-Participantes/<int:id>', views_recorridos.detalle_recorrido,name="MostrarParticipantes"),
    path('calificacion/<int:id>/<int:id_sesion>/', views_recorridos.calificacion, name='RegistrarCalificacion'),
    path('guardarCalificacion/', views_recorridos.registrarCalificacion, name="GuardarCalificacion"),
]

admin.site.index_title="Administración"
admin.site.site_header="BiciTour"
admin.site.site_title="BiciTour"

if settings.DEBUG:

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

