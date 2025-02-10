from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('agregarProyecto/',views.agregarProyecto),
    path('listadoProyectos/',views.listadoProyectos),
    path('guardarProyecto/', views.guardarProyecto),
    path('eliminarProyecto/<int:id>/', views.eliminarProyecto),
    path('editarProyecto/<int:id>/', views.editarProyecto),
    path('procesarEdicionProyecto/', views.procesarEdicionProyecto),

    path('agregarClienteVIP/', views.agregarClienteVIP),
    path('listadoClientesVIP/', views.listadoClientesVIP),
    path('guardarClienteVIP/', views.guardarClienteVIP),
    path('eliminarClienteVIP/<int:id>/', views.eliminarClienteVIP),
    path('editarClienteVIP/<int:id>/', views.editarClienteVIP),
    path('procesarEdicionClienteVIP/', views.procesarEdicionClienteVIP),

    path('agregarVivienda/', views.agregarVivienda),
    path('listadoViviendas/', views.listadoViviendas),
    path('guardarVivienda/', views.guardarVivienda),
    path('eliminarVivienda/<int:id>/', views.eliminarVivienda),
    path('editarVivienda/<int:id>/', views.editarVivienda),
    path('procesarEdicionVivienda/', views.procesarEdicionVivienda),

    path('agregarCosto/', views.agregarCosto),
    path('listadoCostos/', views.listadoCostos),
    path('guardarCosto/', views.guardarCosto),
    path('eliminarCosto/<int:id>/', views.eliminarCosto),
    path('editarCosto/<int:id>/', views.editarCosto),
    path('procesarEdicionCosto/', views.procesarEdicionCosto),
]