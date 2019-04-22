from django.shortcuts import render
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