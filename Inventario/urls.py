from django.conf.urls import url
from Inventario.views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    # ------------- urls base --------------------------------------------
    url(r'^insumo/$',InsumoList.as_view(), name='InsumoList'),
    url(r'^insumoupdate/(?P<nombre>[\w\s]+)/$',InsumoUpdate.as_view(), name='InsumoUpdate'),
    url(r'^insumodelete/(?P<nombre>[\w\s]+)/$',InsumoDelete.as_view(), name='InsumoDelete'),

    url(r'^tipoinsumo/$',TipoInsumoList.as_view(), name='TipoInsumoList'),
    url(r'^tipoinsumoupdate/(?P<nombre>[\w\s]+)/$',TipoInsumoUpdate.as_view(), name='TipoInsumoUpdate'),
    url(r'^tipoinsumoDelete/(?P<nombre>[\w\s]+)/$',TipoInsumoDelete.as_view(), name='TipoInsumoDelete'),

    url(r'^producto/$',ProductoList.as_view(), name='ProductoList'),
    url(r'^productoupdate/(?P<nombre>[\w\s]+)/$',ProductoUpdate.as_view(), name='ProductoUpdate'),
    url(r'^productodelete/(?P<nombre>[\w\s]+)/$',ProductoDelete.as_view(), name='ProductoDelete'),

    url(r'^promocion/$',PromocionList.as_view(), name='PromocionList'),
    url(r'^promocionupdate/(?P<nombre>[\w\s]+)/$',PromocionUpdate.as_view(), name='PromocionUpdate'),
    url(r'^promociondelete/(?P<nombre>[\w\s]+)/$',PromocionDelete.as_view(), name='PromocionDelete'),

    url(r'^promocionproducto/$',PromocionProductoList.as_view(), name='PromocionProductoDetail'),
    # ----------- fin urls base -------------------------------------------    
    url(r'^insumo/(?P<pk>\d+)$',InsumoDetail, name='InsumoDetail'),
    url(r'^promocion/(?P<pk>\d+)$',PromocionDetail, name='PromocionDetail'),

]