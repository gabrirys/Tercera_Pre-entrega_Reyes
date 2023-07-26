from django.contrib import admin
from django.urls import path

from mvt_app.views import ver_usuarios
#from mvt_app.views import

urlpatterns = [
    path("usuarios/", ver_usuarios),
]