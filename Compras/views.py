from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Imports propios
from .models import *
from .serializers import *

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
                'nombre':dato.producto.nombre
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
