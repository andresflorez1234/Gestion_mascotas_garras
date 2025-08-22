from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home'),
    path('inicio/', views.home, name='inicio'),
    path('logout/', views.logout, name='logout'),
    
    # cargos
    path("cargos/", views.lista_cargos, name="cargos"),
    path("cargos/agregar/", views.agregar_cargo, name="agregar_cargo"),
    path("cargos/editar/<int:pk>/", views.editar_cargo, name="editar_cargo"),
    path("cargos/eliminar/<int:pk>/", views.eliminar_cargo, name="eliminar_cargo"),

    # personas
    path("personas/", views.listar_personas, name="personas"),

    # usuarios
    path('usuarios/', views.listar_usuarios, name='usuarios'),
]