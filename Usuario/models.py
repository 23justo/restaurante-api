from django.db import models
from django.conf import settings
from django.contrib import auth
from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Ingrese un nombre de usuario valido.')
        # if not Empleado_id:
        #     raise ValueError('Ingrese un Empleado_id')

        usuario = self.model(
            username = username,
            #Empleado_id = Empleado_id,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, password=None):
        usuario = self.create_user(username, password)
        usuario.is_staff = True

        usuario.set_password(password)
        usuario.save()

        return usuario


class Usuario(AbstractBaseUser):
    user_types = (
    ('Contador','Contador'),
    ('Admin','Admin'),
    ('Mesero','Mesero'),
    )

    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 45,unique = True)
    nombre = models.CharField(max_length = 150)
    email = models.EmailField()
    is_staff = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    ultima_conexion = models.DateTimeField(auto_now_add=True, auto_now=False)
    user_type = models.CharField(max_length=45,choices=user_types,default="Admin")
    compras_modulo = models.BooleanField(default=False)
    inventario_modulo = models.BooleanField(default=False)
    facturacion_modulo = models.BooleanField(default=False)

    
    objects = UsuarioManager()
    USERNAME_FIELD = 'username'
    def get_short_name(self):
        return self.nombre
    def get_type(self):
        return self.user_type
    @property
    def is_admin(self):
        if self.user_type=="Admin":
            return True
        else:
            return False
    def is_contador(self):
        if self.user_type=="Contador":
            return True
        else:
            return False
    def is_mesero(self):
        if self.user_type=="Mesero":
            return True
        else:
            return False
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    def has_module_perms(self,perm_list):
        return self.is_staff
    def has_perm(self,perm):
        return True
