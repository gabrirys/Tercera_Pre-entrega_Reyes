from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    httpResponse = render(
        request=request,
        template_name="base_not.html",
        context={}
        )
    return httpResponse