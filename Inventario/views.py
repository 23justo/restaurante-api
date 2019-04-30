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

class InsumoUpdate(generics.UpdateAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    lookup_field  = 'nombre'

class InsumoDelete(generics.DestroyAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer
    lookup_field  = 'nombre'


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

class TipoInsumoUpdate(generics.UpdateAPIView):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer
    lookup_field  = 'nombre'

class TipoInsumoDelete(generics.DestroyAPIView):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer
    lookup_field  = 'nombre'

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

class ProductoUpdate(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field  = 'nombre'

class ProductoDelete(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field  = 'nombre'

class PromocionList(generics.ListCreateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

class PromocionUpdate(generics.UpdateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    lookup_field  = 'nombre'

class PromocionDelete(generics.DestroyAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    lookup_field  = 'nombre'

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

def PromocionDetail(request,pk):
    promocion = get_object_or_404(Promocion,pk=pk)
    promocionproducto = PromocionProducto.objects.filter(promocion=promocion)
    promocionproducto_dict = {}
    index = 0
    for dato in promocionproducto:
        producto = Producto.objects.get(pk=dato.producto.pk)
        promocionproducto_dict[index] = {
            'id': producto.pk,
            'nombre': producto.nombre,
            'precio': producto.precio
        }
        
        index = index + 1
    data = {
        'pk': promocion.pk,
        'nombre': promocion.nombre,
        'precio': promocion.precio,
        'activa': promocion.activa,
        'productos': promocionproducto_dict
    }
    return JsonResponse(data, safe=False)

def PromocionDetailProductos(request,pk):
    promocion = get_object_or_404(Promocion,pk=pk)
    promocionproducto = PromocionProducto.objects.filter(promocion=promocion)
    promocionproducto_dict = {}
    index = 0
    for dato in promocionproducto:
        producto = Producto.objects.get(pk=dato.producto.pk)
        promocionproducto_dict[index] = {
            'id': producto.pk,
            'nombre': producto.nombre,
            'precio': producto.precio
        }
        
        index = index + 1
    data = {
        'productos': promocionproducto_dict
    }
    return JsonResponse(data, safe=False)

