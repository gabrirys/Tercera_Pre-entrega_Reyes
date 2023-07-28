from django.shortcuts import render, redirect
from django.urls import reverse

from mvt_app.models import Usuario, Contacto, Posteo
from mvt_app.forms import ContactoFormulario, UsuarioFormulario

#VISTAS DE USUARIO
def crear_usuarios(request):
   if request.method == "POST":
       formulario = UsuarioFormulario(request.POST)
       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           apellido = data["apellido"]
           email = data["email"]
           nacimiento = data["nacimiento"]
           usuario = data["usuario"]
           
           # lo crean solo en RAM
           usuario = Usuario(nombre=nombre, apellido=apellido, email=email, nacimiento=nacimiento, usuario=usuario)  
           usuario.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la página ver usuarios
           url_exitosa = reverse('usuarios')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UsuarioFormulario()
   http_response = render(
       request=request,
       template_name='mvt_app/crear_usuarios.html',
       context={'formulario': formulario}
   )
   return http_response


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