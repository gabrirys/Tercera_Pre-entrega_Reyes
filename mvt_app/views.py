from django.shortcuts import render

from mvt_app.models import Usuario, Contacto, Posteo



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
