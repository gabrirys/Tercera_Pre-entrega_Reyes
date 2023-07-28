from django.contrib import admin
from django.urls import path

from mvt_app.views import ver_usuarios, contactar, crear_usuarios, crear_posteo
urlpatterns = [
    path("usuario//", ver_usuarios, name="usuarios"),
    path("crear-usuario/", crear_usuarios, name="crear_usuarios"),
    path("crear-posteo/", crear_posteo, name="crear_posteo"),
    path("contacto/", contactar, name="contacto"),

]