from django.conf.urls import url
from Compras.views import *
from rest_framework.authtoken import views as rest_framework_views
urlpatterns = [
    # ------------- urls base --------------------------------------------
    url(r'^orden/$',OrdenList.as_view(), name='OrdenList'),
    url(r'^ordenactiva/$',OrdenListActivas.as_view(), name='OrdenListActivas'),
    url(r'^ordenproducto/$',OrdenProductoList.as_view(), name='OrdenProductoList'),
    url(r'^ordenproductoactiva/$',OrdenProductoActiva, name='OrdenProductoActiva'),
    url(r'^factura/$',FacturaList.as_view(), name='FacturaList'),
    url(r'^factura/facturar/(?P<pk>\d+)$',facturar, name='Facturar'),
    # ----------- fin urls base -------------------------------------------    
    url(r'^ordenproductodetalle/(?P<pk>\d+)$',OrdenProductoDetalle, name='OrdenProductoDetalle'),
    
]