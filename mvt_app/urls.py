from django.contrib import admin
from django.urls import path

from mvt_app.views import ver_usuario, contactar, crear_usuario, crear_posteo, buscar_usuario
urlpatterns = [
    path("usuarios/", ver_usuario, name="ver_usuarios"),
    path("crear-usuario/", crear_usuario, name="crear_usuarios"),
    path("buscar-usuario/", buscar_usuario, name="buscar_usuarios"),
    path("crear-posteo/", crear_posteo, name="crear_posteos"),
    path("contacto/", contactar, name="contactar"),
]