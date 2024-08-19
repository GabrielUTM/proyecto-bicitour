from datetime import date
from django.shortcuts import render, get_object_or_404
from .forms import RegistroParticipantesForm, ComentarioForm
from .models import Recorridos, Inscripcion

# Create your views here.

# Vista Detalle Recorrido.
# En esta vista se muestran los atributos del recorrido almacenado en la tabla
# Es una función que renderiza una vista basado en los objetos que recibe de las tablas.
def detalle_recorrido(request, id):
    #Recibe datos de la tabla recorrido y inscripciones 
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)
    inscripcion = request.COOKIES.get('inscripcion')
    recorrido_id = request.COOKIES.get('recorrido_id')
    vacio = False
    
    #Y en caso de que la inscripción o cookie exista, envia los datos para su procesamiento
    if inscripcion != None:
        sesion = get_object_or_404(Inscripcion, id_inscripcion=inscripcion)
    else:
        sesion = None
    if recorrido_id != None:
        sesion_recorrido =get_object_or_404(Recorridos, id_recorrido=recorrido_id)
    else:
        sesion_recorrido = None

    if not inscripciones.exists():
        vacio = True
    
    # Para Finalizar se cargan los datos en la vista.    
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'inscripciones': inscripciones,'sesion':sesion ,'vacio': vacio, 'sesion_recorrido': sesion_recorrido})

# Función calificación
# Es una vista que en la vista detalle de recorrido el cual despliega un modal para despues calificar
def calificacion(request, id, id_sesion):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    sesion = get_object_or_404(Inscripcion, id_inscripcion=id_sesion)
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)  
    vacio = False
    if not inscripciones.exists():
        vacio = True
        
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido, 'sesion':sesion, 'inscripciones': inscripciones, 'vacio':vacio})

# Vista registrar calificación
# Esta vista permite a traves de un modal enviar la calificación de un recorrido a la base de datos
def registrarCalificacion(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    inscripcion = request.COOKIES.get('inscripcion')
    recorrido_id = request.COOKIES.get('recorrido_id')
    inscripciones = Inscripcion.objects.filter(id_recorrido=id)
    vacio = False
    
    #Si los datos no estan vacios entonces envia los datos a la BD            
    if inscripcion != None:
        sesion = get_object_or_404(Inscripcion, id_inscripcion=inscripcion)
    else:
        sesion = None
    if recorrido_id != None:
        sesion_recorrido =get_object_or_404(Recorridos, id_recorrido=recorrido_id)
    else:
        sesion_recorrido = None

    if not inscripciones.exists():
        vacio = True
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            comentario_exitoso = True
            return render(request, "recorridos/detalle_recorrido.html", {'recorrido':recorrido, 'comentario_exitoso': comentario_exitoso, 'vacio':vacio, 'sesion':sesion, 'sesion_recorrido': sesion_recorrido, 'inscripciones':inscripciones})
        else:
            return render(request, "recorridos/detalle_recorrido.html", {'form':form, 'recorrido': recorrido})
    form = ComentarioForm()
    return render(request, "recorridos/detalle_recorrido.html", {'form':form, 'recorrido': recorrido})       

# Vista que obtiene los recorridos activos
def recorridosProximos(request):
    recorridos = Recorridos.objects.filter(activo=True)
    is_today = date.today()
    inscripcion = 'form' in request.COOKIES
    return render(request, "recorridos/recorridos.html", {'recorridos': recorridos, 'is_today': is_today})

# Vista que obtiene los recorridos finalizados
def recorridosFinalizados(request):
    recorridos = Recorridos.objects.filter(activo=False)
    return render(request, "recorridos/recorridos.html", {'recorridos': recorridos})

# Vista para enviar el formulario de registro
def pre_registro(request, id):
    recorrido = get_object_or_404(Recorridos, id_recorrido = id)
    return render(request, "recorridos/pre-registro.html", {'recorrido': recorrido})

# Vista para guardar los participantes.
# Recibe los datos anteriores enviados en pre-registro y los guarda en la BD
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
            respuesta.set_cookie('recorrido_id', id, path='/')
            """             imprimir = request.COOKIES.get('inscripcion')
            imprimir2 = request.COOKIES.get('recorrido_id')
            print(imprimir)
            print(imprimir2) """
            return respuesta
        else:
            return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    form = RegistroParticipantesForm()
    return render(request, "recorridos/pre-registro.html", {'form': form, 'recorrido': recorrido})
    
