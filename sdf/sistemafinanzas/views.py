from django.shortcuts import render

# Create your views here.
from sistemafinanzas.models import Credito


def listar_creditos(request):
    """" Lista todos los creditos con estado pendiente """

    creditos = Credito.objects.filter(estado="Pendiente")


    return render(request, "listar-creditos.html/" , {'creditos': creditos})

def ver_credito(request, credito_id):
    """" Muestra el credito seleccionado """


    credito = Credito.objects.filter(pk=credito_id)

    return render(request, "ver-credito.html/", {"credito": credito})

def aprobar_credito(request, credito_id):
    """" Realiza la aprobacion del credito elegido """

    credito = Credito.objects.filter(pk=credito_id)

    credito.estado("Aprobado")


    return render(request, "/ver-creditos.html/credito_id", {"credito":credito})


def desaprobar_credito(request, credito_id):
    """" Realiza la desaprobacion del credito elegido """

    credito = Credito.objects.filter(pk=credito_id)

    credito.estado("Denegado")

    return render(request, "/ver-creditos.html/credito_id", {"credito":credito})