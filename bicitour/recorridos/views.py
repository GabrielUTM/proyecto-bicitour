from django.shortcuts import render

# Create your views here.
def detalle_recorrido(request):
    return render(request, "recorridos/detalle_recorrido.html")

def recorridos(request):
    return render(request, "recorridos/recorridos.html")