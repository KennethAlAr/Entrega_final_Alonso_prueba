from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse # Esto sirve para poder enviar strings a django.

from .models import Reserva

def home_view(request): # Las funciones en url siempre reciben un argumento cuando hacemos funcionar el servidor.
    return HttpResponse("<h3>Bienvenidos a la home de reservas 'Bookings'!!!</h3>") # El HttpResponse se usa aquí para enviar strings.

# def list_view(request):
#     contexto_dict = {
#         'reservas': [
#             {"usuario": "Emiliano Martínez ", "destino": "aruba"},
#             {"usuario": "Nicolas Otamendi ", "destino": "italia"},
#             {"usuario": "Nahuel Molina ", "destino": "multidestino"},
#             {"usuario": "Gonzalo Montiel ", "destino": "inglaterra"},
#             {"usuario": "Lisando Martinez ", "destino": "mexico"},
#             {"usuario": "Angel di maria", "destino": "uruguay"},
#             {"usuario": "Julián Álvarez", "destino": "albania"},
#         ]
#     }
#     # return HttpResponse("<h3<Listado de reservas</h3>")
#     return render(request, "list.html", contexto_dict)

def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'reservas': reservas}
    return render(request, "bookings/list.html", contexto_dict)

def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict2 = {"reservas": reservas_del_usuario}
    return render(request, "bookings/list.html", contexto_dict2)
    # reservas = []
    # for reserva in reservas_del_usuario:
    #     reservas.append(reserva)
    # return HttpResponse(reservas)

def create_view(request, nombre_de_usuario, destino):

    # reserva = Reserva("", nombre_de_usuario, destino)
    reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, destino=destino)

    return HttpResponse(f"Resultado: {reserva}")