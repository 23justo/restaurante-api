from .models import *
from rest_framework.serializers import ModelSerializer

class InsumoSerializer(ModelSerializer):
    class Meta:
        model = Insumo
        fields = ('id','nombre','tipo_insumo')

class TipoInsumoSerializer(ModelSerializer):
    class Meta:
        model = TipoInsumo
        fields = ('id','nombre','producto')

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','nombre','precio')
    
    def __str__(self):
        return self.nombre

class PromocionSerializer(ModelSerializer):
    class Meta:
        model = Promocion
        fields = ('id','nombre','precio')

class PromocionProductoSerializer(ModelSerializer):
    class Meta:
        model = PromocionProducto
        fields = ('id','producto','promocion')
