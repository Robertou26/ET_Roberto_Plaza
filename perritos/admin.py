from django.contrib import admin
from .models import Categoria, Perrito,detalle_boleta,Boleta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Perrito)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)