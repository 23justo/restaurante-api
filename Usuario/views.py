from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Imports propios
from .models import *
from .serializers import *
from django.views.generic import ListView, TemplateView,View,DetailView
# Create your views here.

class InicioView(TemplateView):
    template_name = "Templates/index.html"

class AutenticacionView(TemplateView):
    template_name = "Templates/autenticacion.html"

class InsumoView(TemplateView):
    template_name = "Templates/insumo.html"

class TipoInsumoView(TemplateView):
    template_name = "Templates/tipoinsumo.html"

class ProductoView(TemplateView):
    template_name = "Templates/producto.html"

class PromocionView(TemplateView):
    template_name = "Templates/promocion.html"

class PromocionProductoView(TemplateView):
    template_name = "Templates/promocionproducto.html"

class OrdenView(TemplateView):
    template_name = "Templates/orden.html"

class UsuarioView(TemplateView):
    template_name = "Templates/usuario.html"


# vistas de modulo



class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk'],
        )
        return obj

def UsuarioDetalle(request,pk):
    usuario = get_object_or_404(Usuario,pk=pk)
    data = {
        'Usuario':{
            'id': usuario.pk,
            'username': usuario.username,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'is_staff': usuario.is_staff,
            'is_active': usuario.is_active,
            'ultima_conexion': usuario.ultima_conexion,
            'user_type': usuario.user_type,
            'compras_modulo': usuario.compras_modulo,
            'inventario_modulo': usuario.inventario_modulo,
            'facturacion_modulo': usuario.facturacion_modulo
        }
    }
    return JsonResponse(data, safe=False)

def UsuarioDetalleUsername(request,username):
    usuario = get_object_or_404(Usuario,username=username)
    data = {
        'Usuario':{
            'id': usuario.pk,
            'username': usuario.username,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'is_staff': usuario.is_staff,
            'is_active': usuario.is_active,
            'ultima_conexion': usuario.ultima_conexion,
            'user_type': usuario.user_type,
            'compras_modulo': usuario.compras_modulo,
            'inventario_modulo': usuario.inventario_modulo,
            'facturacion_modulo': usuario.facturacion_modulo
        }
    }
    return JsonResponse(data, safe=False)
