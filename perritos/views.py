from django.shortcuts import render, redirect
from .models import Perrito, Boleta, detalle_boleta
from .forms import PerritoForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from perritos.compra import Carrito


# Create your views here.
def index(request):
    return render(request, 'index.html')

def otra(request):
    perritos= Perrito.objects.raw('Select * from perritos_perrito')
    datos={
        'caninos':perritos
    }
    return render(request, 'otra.html', datos)

def categoria(request):
    return render(request, 'categoria.html')


def galeria(request):
    return render(request, 'galeria.html')


def info(request):
    return render(request, 'info.html')
@login_required
def crear(request):
    if request.method=="POST":
        perritoform = PerritoForm(request.POST, request.FILES)
        if perritoform.is_valid():
            perritoform.save()     #similar al insert
            return redirect('otra')
    else:
        perritoform=PerritoForm()
    return render(request, 'crear.html', {'perritoform':perritoform})

@login_required
def eliminar(request, id):
    PerritoEliminado = Perrito.objects.get(id=id) #obtenemos un objeto por su id
    PerritoEliminado.delete()
    return redirect ('otra')
    


@login_required
def modificar(request, id):
    perrito = Perrito.objects.get(id=id)
    datos = {
        'form': PerritoForm(instance=perrito)
    }
    if request.method=='POST':
        formulario = PerritoForm(data=request.POST, instance=perrito)
        if formulario.is_valid:
            formulario.save()
            return redirect('otra')
    return render(request, 'modificar.html', datos)


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)


def mostrar(request):
    caninos = Perrito.objects.all()
    datos={
        'caninos':caninos
    }
    return render(request,'mostrar.html',datos)

def tienda(request):
    caninos = Perrito.objects.all()
    datos={
        'caninos':caninos
    }
    return render(request, 'tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    perrito = Perrito.objects.get(id=id)
    carrito_compra.agregar(perrito=perrito)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    perrito = Perrito.objects.get(id=id)
    carrito_compra.eliminar(perrito=perrito)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    perrito = Perrito.objects.get(id=id)
    carrito_compra.restar(perrito=perrito)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Perrito.objects.get(id = value['perrito_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)