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
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('recorridos/', views_recorridos.recorridos, name="Recorridos"),
    path('detalle/', views_recorridos.detalle_recorrido, name="Detalle"),
]

if settings.DEBUG:

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

