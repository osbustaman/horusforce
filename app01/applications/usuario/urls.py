from django.urls import path

from applications.usuario.api.api import (
    ColaboradorCreateAPIView
    , ColaboradorUpdateAPIView
    , ColaboradorDetailApiView
    , UsuarioEmpresaDatosLaboralesCreateAPIView
    , UsuarioEmpresaDatosLaboralesDetailApiView
    , UsuarioEmpresaDatosLaboralesUpdateView
)


app_name = 'usuario_app'

urlpatterns = [
    path('colaborador/add/', ColaboradorCreateAPIView.as_view(), name='add-colaborador'),
    path('colaborador/edit/<pk>/', ColaboradorUpdateAPIView.as_view(), name='edit-colaborador'),
    path('colaborador/search/<pk>/', ColaboradorDetailApiView.as_view(), name='search-colaborador'),
    path('colaborador/add/labor-data/<user_id>/', UsuarioEmpresaDatosLaboralesCreateAPIView.as_view(), name='add-labor-data-colaborador'),
    path('colaborador/edit/labor-data/<pk>/', UsuarioEmpresaDatosLaboralesUpdateView.as_view(), name='edit-labor-data-colaborador'),
    path('colaborador/search/labor-data/<pk>/', UsuarioEmpresaDatosLaboralesDetailApiView.as_view(), name='search-labor-data-colaborador'),
]