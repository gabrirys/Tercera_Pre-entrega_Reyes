from django import forms


class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    email = forms.EmailField(required=True)
    nacimiento = forms.DateField()
    usuario = forms.CharField(required=True, max_length=64)


class ContactoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=128)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=20)
    mensaje = forms.CharField(required=True, widget=forms.Textarea)