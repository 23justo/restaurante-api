from django.shortcuts import render
from django.views.generic import ListView, TemplateView,View,DetailView
# Create your views here.

class InicioView(TemplateView):
    template_name = "Templates/index.html"

class AutenticacionView(TemplateView):
    template_name = "Templates/autenticacion.html"