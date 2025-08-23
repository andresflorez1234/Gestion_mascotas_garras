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
    path("crear/", views.crear_persona, name="crear_persona"),
    path("editar/<int:id_persona>/", views.editar_persona, name="editar_persona"),
    path("eliminar/<int:id_persona>/", views.eliminar_persona, name="eliminar_persona"),

    # usuarios
    path('usuarios/', views.listar_usuarios, name='usuarios'),
    path("usuarios/crear/", views.crear_usuario, name="crear_usuario"),
    path("usuarios/editar/<int:id_persona>/<int:id_tipo>/", views.editar_usuario, name="editar_usuario"),
    path("usuarios/eliminar/<int:id_persona>/<int:id_tipo>/", views.eliminar_usuario, name="eliminar_usuario"),
]