from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Insumo(models.Model):
    nombre = models.CharField(max_length=250,unique= True)
    tipo_insumo  = models.ForeignKey('TipoInsumo')
    def __str__(self):
        return self.nombre

class TipoInsumo(models.Model):
    nombre = models.CharField(max_length=250, unique= True)
    producto  = models.ForeignKey('Producto')
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=250, unique= True)
    precio = models.FloatField(validators=[MinValueValidator(0)])
    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    nombre = models.CharField(max_length=250, unique= True)
    precio = models.FloatField(validators=[MinValueValidator(0)])
    activa = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class PromocionProducto(models.Model):
    producto  = models.ForeignKey('Producto')
    promocion  = models.ForeignKey('Promocion')
    def __str__(self):
        return "promocionproducto"

