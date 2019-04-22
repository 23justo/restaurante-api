"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from rest_framework.authtoken import views as rest_framework_views
from Usuario.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('Inventario.urls', namespace='Inventario')),
    url(r'^api/v1/compras/', include('Compras.urls', namespace='Compras')),
    # docs
    url(r'^$', InicioView.as_view(), name='InicioView'),
    url(r'^autenticacion/$', AutenticacionView.as_view(), name='AutenticacionView'),
    url(r'^insumo/$', InsumoView.as_view(), name='InsumoView'),
    url(r'^tipoinsumo/$', TipoInsumoView.as_view(), name='TipoInsumoView'),
    url(r'^producto/$', ProductoView.as_view(), name='ProductoView'),
    url(r'^promocion/$', PromocionView.as_view(), name='PromocionView'),
    url(r'^promocionproducto/$', PromocionProductoView.as_view(), name='PromocionProductoView'),


    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
urlpatterns += [
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', rest_framework_views.obtain_auth_token, name="api-token-auth"),

]

