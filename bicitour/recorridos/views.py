from django.shortcuts import render
from .forms import RegistroParticipantesForm
from .models import Recorridos

# Create your views here.
def detalle_recorrido(request, id):
    recorrido = Recorridos.objects.get(id_recorrido=id)
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido})

def recorridos(request):
    recorridos = Recorridos.objects.all()
    return render(request, "recorridos/recorridos.html", {'recorridos': recorridos})

def pre_registro(request):
    return render(request, "recorridos/pre-registro.html")

def consultarRecorrido(request, id):
    recorrido = Recorridos.objects.get(id=id)
    
    return render(request, "recorridos/detalle_recorrido.html", {'recorrido': recorrido})

def registrarParticipante(request, id_recorrido):
    if request.method == 'POST':
        form = RegistroParticipantesForm(request.POST)
        if form.is_valid():
            form.save()
