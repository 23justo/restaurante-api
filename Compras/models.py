from django.db import models
from Inventario.models import Producto
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Orden(models.Model):
    numero_mesa = models.CharField(max_length=10)
    activa = models.BooleanField(default=True)
    def __str__(self):
        return self.numero_mesa

class OrdenProducto(models.Model):
    estado = (
        ('Entregado','Entregado'),
        ('Preparando','Preparando'),
        ('en_espera','En espera')
    )
    ('En espera','en_espera')
    orden = models.ForeignKey('Orden')
    producto = models.ForeignKey(Producto)
    estado = models.CharField(max_length=250, choices=estado)
    def __str__(self):
        return self.orden.numero_mesa + self.producto.nombre

class Factura(models.Model):
    orden = models.ForeignKey('Orden')
    correlativo = models.IntegerField(validators=[MinValueValidator(0)])
    encargado = models.ForeignKey('Usuario.Usuario',null = True, blank = True)
