from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import RegistroParticipantesForm
from .models import Recorridos, Inscripcion

# Create your views here.
def detalle_recorrido(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    inscripciones = get_list_or_404(Inscripcion, id_recorrido=id)
    inscripcion = 'form' in request.COOKIES
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'inscripcion_existe':inscripcion, 'inscripciones': inscripciones})

def recorridosProximos(request):
    recorridos = Recorridos.objects.filter(activo=True)
    return render(request, "recorridos/recorridos.html", {'recorridos': recorridos})

def recorridosFinalizados(request):
    recorridos = Recorridos.objects.filter(activo=False)
    return render(request, "recorridos/recorridos.html", {'recorridos': recorridos})

def pre_registro(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    return render(request, "recorridos/pre-registro.html", {'recorrido': recorrido})

def registrarParticipante(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido=id)
    if request.method == 'POST':
        form = RegistroParticipantesForm(request.POST)
        if form.is_valid():
            form.save()
            recorrido = get_object_or_404(Recorridos, id_recorrido = id)
            respuesta = render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'inscripcion_existe':'form' in request.COOKIES })
            respuesta.set_cookie('form', 'true', path='/')
            return respuesta
        else:
            return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    form = RegistroParticipantesForm()
    return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    
