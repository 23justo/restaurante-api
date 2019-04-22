from django.conf.urls import url
from Compras.views import *
from rest_framework.authtoken import views as rest_framework_views
urlpatterns = [
    # ------------- urls base --------------------------------------------
    url(r'^orden/$',OrdenList.as_view(), name='OrdenList'),
    url(r'^ordenproducto/$',OrdenProductoList.as_view(), name='OrdenProductoList'),
    url(r'^factura/$',FacturaList.as_view(), name='FacturaList'),
    # ----------- fin urls base -------------------------------------------    
    url(r'^ordenproductodetalle/(?P<pk>\d+)$',OrdenProductoDetalle, name='OrdenProductoDetalle'),
    
]