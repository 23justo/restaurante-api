from django.conf.urls import url
from Inventario.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    # ------------- urls base --------------------------------------------
    url(r'^insumo/$',InsumoList.as_view(), name='InsumoList'),
    url(r'^insumoupdate/(?P<nombre>\w+)/$',InsumoUpdate.as_view(), name='InsumoUpdate'),
    url(r'^tipoinsumo/$',TipoInsumoList.as_view(), name='TipoInsumoList'),
    url(r'^tipoinsumoupdate/(?P<nombre>\w+)/$',TipoInsumoUpdate.as_view(), name='TipoInsumoUpdate'),
    url(r'^producto/$',ProductoList.as_view(), name='ProductoList'),
    url(r'^productoupdate/(?P<nombre>\w+)/$',ProductoUpdate.as_view(), name='ProductoUpdate'),
    url(r'^promocion/$',PromocionList.as_view(), name='PromocionList'),
    url(r'^promocionproducto/$',PromocionProductoList.as_view(), name='PromocionProductoDetail'),
    # ----------- fin urls base -------------------------------------------    
    url(r'^insumo/(?P<pk>\d+)$',InsumoDetail, name='InsumoDetail'),
    url(r'^promocion/(?P<pk>\d+)$',PromocionDetail, name='PromocionDetail'),

]