from django.conf.urls import url
from Usuario.views import *

urlpatterns = [
    # ------------- urls base --------------------------------------------
    url(r'^usuario/$',UsuarioList.as_view(), name='UsuarioList'),
    url(r'^usuario/(?P<pk>\d+)$',UsuarioDetalle, name='UsuarioDetalle'),
    # ----------- fin urls base -------------------------------------------    
]