from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from random import randint
# Imports propios
from .models import *
from .serializers import *
from Inventario.models import *
from Usuario.models import *

class OrdenList(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class OrdenListActivas(generics.ListCreateAPIView):
    queryset = Orden.objects.filter(activa = True)
    serializer_class = OrdenSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj
    def get_queryset(self):
        
        return queryset

def OrdenProductoActiva(request):
    orden = Orden.objects.filter(activa = True)
    ordenes = {}
    contador_orden = 0
    for orden_dato in orden:
        ordenes_dict_temporal = {}
        ordenproducto = OrdenProducto.objects.filter(orden=orden_dato)
        productos = {}
        contador = 0
        total = 0
        for dato in ordenproducto:
            diccionario = {}
            total += dato.producto.precio
            contador = contador + 1
            diccionario = {
                dato.pk:{
                    'nombre':dato.producto.nombre,
                    'estado':dato.estado
                }
            }
            productos.update(diccionario)
        data = {
            contador_orden:{
                'OrdenProducto':{
                    'Orden':{
                        'pk':orden_dato.pk,
                        'numero_mesa':orden_dato.numero_mesa
                    },
                    'Productos':productos,
                    'Total': total
                }
            }
        }
        ordenes.update(data)
        contador_orden = contador_orden + 1
    return JsonResponse(ordenes, safe=False)



class OrdenProductoList(generics.ListCreateAPIView):
    queryset = OrdenProducto.objects.all()
    serializer_class = OrdenProductoSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class FacturaList(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

def OrdenProductoDetalle(request,pk):
    orden = get_object_or_404(Orden,pk=pk)
    ordenproducto = OrdenProducto.objects.filter(orden=orden)
    productos = {}
    contador = 0
    total = 0
    for dato in ordenproducto:
        diccionario = {}
        total += dato.producto.precio
        contador = contador + 1
        diccionario = {
            dato.pk:{
                'nombre':dato.producto.nombre,
                'estado':dato.producto.estado
            }
        }
        productos.update(diccionario)
    data = {
        'OrdenProducto':{
            'Orden':{
                'pk':orden.pk,
                'numero_mesa':orden.numero_mesa
            },
            'Productos':productos,
            'Total': total
        }
    }
    return JsonResponse(data, safe=False)

# pk pertenece a una orden
def facturar(request,pk):
    orden = get_object_or_404(Orden,pk=pk)
    usuario = Usuario.objects.get(pk = request.user.pk)
    orden.activa = False
    orden.save()
    factura = Factura(
        orden = orden,
        correlativo = randint(0, 9999999999),
        encargado = usuario,
    )
    factura.save()
    data = {
        'mensaje': 'Se ha facturado exitosamente.',

    }
    return JsonResponse(data, safe=False)

