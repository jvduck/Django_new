# aqui crearemos nuestras forms para hacer todo mas EFICIENE en el manejo de Django
#? Ventaja: Velocidad de procesamiento de campos necesarios, al igual que el uso de VALIDACIONES que tiene el forms
#!Desventaja: Forms requiere q los estilos les sean dados desde CSS. Esto debido a que no tendremos acceso desde HTML

#Django se encarga de crear el HTML necesario q será renderizado del lado del cliente
from django import forms
from .models import Productos

class FormProducto(forms.ModelForm):
    
    class Meta:
        error = "Error found in the form"
        model = Productos
        fields = '__all__'
        