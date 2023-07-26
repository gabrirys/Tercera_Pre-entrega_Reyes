from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    nacimiento = models.DateField(null=True)
    usuario = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.usuario})"
        
     
class Posteo(models.Model):
    titulo = models.CharField(max_length=128)
    contenido = models.TextField(blank=True)
    fecha_publicado = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=64)
    #imagen?
    def __str__(self):
        return f"{self.titulo} - {self.autor} -" 
     
     
class Contacto(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}"
