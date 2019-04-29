from .models import *
from rest_framework.serializers import ModelSerializer

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'nombre',
            'email',
            'is_staff',
            'is_active',
            'ultima_conexion',
            'user_type',
            'compras_modulo',
            'inventario_modulo',
            'facturacion_modulo'
        )
        