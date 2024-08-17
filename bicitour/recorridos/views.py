from django.shortcuts import render, get_object_or_404
from .forms import RegistroParticipantesForm, ComentarioForm
from .models import Recorridos, Inscripcion

# Create your views here.
def detalle_recorrido(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)
    inscripcion = request.COOKIES.get('inscripcion')
    if inscripcion != None:
        sesion = get_object_or_404(Inscripcion, id_inscripcion=inscripcion)
    else:
        sesion = "Sin sesion"
    # print(sesion.usuario_nombre)
    
    vacio = False
    
    if not inscripciones.exists():
        vacio = True
        
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'inscripciones': inscripciones,'sesion':sesion ,'vacio': vacio})

def calificacion(request, id, id_sesion):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    sesion = get_object_or_404(Inscripcion, id_inscripcion=id_sesion)
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)  
    vacio = False
    if not inscripciones.exists():
        vacio = True
        
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'sesion':sesion, 'inscripciones': inscripciones, 'vacio':vacio})

def registrarCalificacion(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            comentario_exitoso = True
            return render(request, "recorridos/detalle_recorrido.html", {'recorrido':recorrido, 'comentario_exitoso': comentario_exitoso})
        else:
            return render(request, "recorridos/detalle_recorrido.html", {'form':form, 'recorrido': recorrido})
    form = ComentarioForm()
    return render(request, "recorridos/detalle_recorrido.html", {'form':form, 'recorrido': recorrido})       

def recorridosProximos(request):
    recorridos = Recorridos.objects.filter(activo=True)
    inscripcion = 'form' in request.COOKIES
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
            inscripcion = form.save()
            recorrido = get_object_or_404(Recorridos, id_recorrido = id)
            inscripciones = Inscripcion.objects.filter(id_recorrido = id)
            exitoso = True
            respuesta = render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido,'inscripciones':inscripciones, 'exitoso':exitoso ,'inscripcion':'inscripcion' in request.COOKIES })
            respuesta.set_cookie('inscripcion', inscripcion.id_inscripcion, path='/')
            imprimir = request.COOKIES.get('inscripcion')
            print(imprimir)
            return respuesta
        else:
            return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    form = RegistroParticipantesForm()
    return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    
