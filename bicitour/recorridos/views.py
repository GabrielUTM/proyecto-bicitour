from django.shortcuts import render, get_object_or_404, get_list_or_404
from .forms import RegistroParticipantesForm, ComentarioForm
from .models import Recorridos, Inscripcion, Comentario

# Create your views here.
def detalle_recorrido(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)
    inscripcion = request.COOKIES.get('inscripcion')
    sesion = get_object_or_404(Inscripcion, id_inscripcion=inscripcion)
    
    print(sesion.usuario_nombre)
    if not inscripciones.exists():
        inscripciones = "No hay participantes en el recorrido"
        
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'sesion':sesion, 'inscripciones': inscripciones})

def calificacion(request, id, id_sesion):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    sesion = get_object_or_404(Inscripcion, id_inscripcion=id_sesion)
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)  
    
    if not inscripciones.exists():
        inscripciones = "No hay participantes en el recorrido"
        
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'sesion':sesion, 'inscripciones': inscripciones})

def registrarCalificacion(request):
    recorrido = Recorridos.objects.all()
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            
            id_inscripcion = int(request.POST.get('id_inscripcion'))
            id_recorrido = int(request.POST.get('id_recorrido'))
            
            comentario.id_inscripcion = id_inscripcion
            comentario.id_recorrido = id_recorrido
            
            comentario.save()
            return render(request, "recorridos/recorridos.html", {'recorridos':recorrido})
        else:
            form = ComentarioForm()
    
    return render(request, "principal/principal.html")        

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
            respuesta = render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'inscripcion':'inscripcion' in request.COOKIES })
            respuesta.set_cookie('inscripcion', inscripcion.id_inscripcion, path='/')
            imprimir = request.COOKIES.get('inscripcion')
            print(imprimir)
            return respuesta
        else:
            return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    form = RegistroParticipantesForm()
    return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    
