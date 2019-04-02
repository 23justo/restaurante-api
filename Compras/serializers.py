from .models import *
from rest_framework.serializers import ModelSerializer

class OrdenSerializer(ModelSerializer):
    class Meta:
        model = Orden
        fields = ('id','numero_mesa',)

class OrdenProductoSerializer(ModelSerializer):
    class Meta:
        model = OrdenProducto
        fields = ('id','producto','orden','estado')

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Factura
        fields = ('id','correlativo','orden')