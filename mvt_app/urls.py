from django.contrib import admin
from django.urls import path

from mvt_app.views import ver_usuarios, contactar
urlpatterns = [
    path("usuario//", ver_usuarios, name="usuarios"),
    #path("crear-usuario/", crear_usuarios, name="crear_usuarios"),
    
    path("contacto/", contactar, name="contacto"),

]