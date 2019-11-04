from django.urls import path
from .views import home, galeria, formulario, listar_clientes, eliminar_cliente,  modificar_cliente

urlpatterns = [
    path('',home, name="home"),
    path('galeria/',galeria, name="galeria"),
    path('formulario/',formulario, name="formulario"),
    path('listar-clientes/', listar_clientes, name="listado_clientes"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
]
