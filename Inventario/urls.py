from django.conf.urls import url
from Inventario.views import *

urlpatterns = [
    # ------------- urls base --------------------------------------------
    url(r'^insumo/$',InsumoList.as_view(), name='InsumoList'),
    url(r'^tipoinsumo/$',TipoInsumoList.as_view(), name='TipoInsumoList'),
    url(r'^producto/$',ProductoList.as_view(), name='ProductoList'),
    url(r'^promocion/$',PromocionList.as_view(), name='PromocionList'),
    url(r'^promocionproducto/$',PromocionProductoList.as_view(), name='PromocionProductoDetail'),
    # ----------- fin urls base -------------------------------------------    
    url(r'^insumo/(?P<pk>\d+)$',InsumoDetail, name='InsumoDetail'),
    url(r'^promocion/(?P<pk>\d+)$',PromocionDetail, name='PromocionDetail'),

]