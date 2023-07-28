from django import forms

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=128)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(max_length=20)
    mensaje = forms.CharField(required=True, widget=forms.Textarea)