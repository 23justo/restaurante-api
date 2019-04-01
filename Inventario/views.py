from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Imports propios
from .models import *
from .serializers import *


class InsumoList(generics.ListCreateAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class TipoInsumoList(generics.ListCreateAPIView):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class PromocionList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class PromocionProductoList(generics.ListCreateAPIView):
    queryset = PromocionProducto.objects.all()
    serializer_class = PromocionProductoSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

def InsumoDetail(request,pk):
    insumo = get_object_or_404(Insumo,pk=pk)
    data = {
        'pk': insumo.pk,
        'nombre': insumo.nombre,
        'tipo_insumo': {
            'pk': insumo.tipo_insumo.pk,
            'nombre': insumo.tipo_insumo.nombre,
            'producto': {
                'pk': insumo.tipo_insumo.producto.pk,
                'nombre': insumo.tipo_insumo.producto.nombre,
                'precio': insumo.tipo_insumo.producto.precio,
            }
            
        }
    }
    return JsonResponse(data, safe=False)

