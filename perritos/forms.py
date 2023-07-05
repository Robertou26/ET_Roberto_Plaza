from django import forms
from .models import Perrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class PerritoForm(forms.ModelForm):
    class Meta:
        model = Perrito                #nombre de la clase
        fields = ['id', 'marca', 'raza', 'producto','categoria','precio', 'imagen'] #atributos de la clase
        labels = {                     #etiquetas asociadas a los atributos
            'Id': 'Id',
            'marca' : 'Marca',
            'raza' : 'Raza',
            'producto': 'Producto',
            'categoria': 'Categoria',
            'precio':'Precio',
            'imagen' : 'Imagen'
        }
        widgets = {
            'id' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder': 'Ingrese id..',
                    'id':'id',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese marca..',
                    'id':'marca',
                }
            ),
            'raza': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese raza..',
                    'id':'raza',
                }
            ),
            'producto':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Seleccione producto..',
                    'id':'producto',
                }
            ),
            'Categoria': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Seleccione la categoria...',
                    'id':'categoria',
                }
            ),            
            'precio': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese Cantidad..',
                    'id':'precio',
                }
            ),        
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen',
                }
            ),

        }#cierre de widgets
