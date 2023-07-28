from django.shortcuts import render, redirect
from django.urls import reverse

from mvt_app.models import Usuario, Contacto, Posteo
from mvt_app.forms import ContactoFormulario

#VISTAS DE USUARIO
#def crear_usuario(request):


def ver_usuarios(request):
    contexto = {
            "usuarios": Usuario.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="mvt_app/ver_usuarios.html",
        context=contexto,
        )
    return http_response
    

#VISTAS DE POSTEO
def ver_posteo(request):
    contexto = {
            "posteo": Posteo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="mvt_app/ver_post.html",
        context=contexto,
        )
    return http_response




#VISTA DE CONTACTO
def contactar(request):
   if request.method == "POST":
       formulario = ContactoFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           email = data["email"]
           telefono = data["telefono"]
           mensaje = data["mensaje"]
           
           contacto = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)  # lo crean solo en RAM
           contacto.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la página inicio
           url_exitosa = reverse('inicio')  # me regresa a inicio
           return redirect(url_exitosa)
   else:  # GET
       formulario = ContactoFormulario()
   http_response = render(
       request=request,
       template_name='mvt_app/contacto.html',
       context={'formulario': formulario}
   )
   return http_response