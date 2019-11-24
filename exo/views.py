from django.shortcuts import render, get_object_or_404
from .models import Usuario, Productos
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage

# Create your views here.

def init(request):
    return render(request, 'exo/index.html')

def post_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'blog/post_list.html', {'jh': usuarios})

def detalle_usuario(request, pk):
    a = get_object_or_404(Usuario, pk=pk)
    return render(request, 'blog/detalle_usuario.html', {'deta': a})

def menu_cafe(request):
    productos = Productos.objects.all()
    return render(request, 'exo/menucafe.html', {"productos": productos})

def registro(request):
    return render(request, 'exo/cuestionario.html')

def ejemplocrud(request):
    productos = Productos.objects.all()
    return render(request, 'exo/ejemplocrud.html', {"productos": productos})

def crudcrear(request):
    if request.method == "GET":
        return render(request, 'exo/crudcrear.html')
    producto = Productos()
    producto.pk = request.POST.get("id")
    producto.nombre = request.POST.get("nombre")
    producto.descripcion = request.POST.get("descripcion")
    if request.FILES['imagen']:
        producto.imagenes = request.FILES['imagen']
    producto.valor = request.POST.get("valor")
    producto.cantidad = request.POST.get("cantidad")

    producto.save()

    return HttpResponseRedirect('/ejemplocrud/')


def crudeliminar(request, pk):
    if request.method == "GET":
        producto = get_object_or_404(Productos, pk=pk)
        return render(request, 'exo/crudeliminar.html', {"producto": producto})
    pk = request.POST.get("pk")
    #print("asdasd "+pk)
    producto = get_object_or_404(Productos, pk=pk)
    producto.delete()
    return HttpResponseRedirect('/ejemplocrud/')


def crudeditar(request, pk):
    if request.method == "GET":
        producto = get_object_or_404(Productos, pk=pk)
        return render(request, 'exo/crudeditar.html', {"producto": producto})
    producto = Productos()
    producto.pk = request.POST.get("id")
    producto.nombre = request.POST.get("nombre")
    producto.descripcion = request.POST.get("descripcion")
    if request.FILES['imagen']:
        producto.imagenes = request.FILES['imagen']
    producto.valor = request.POST.get("valor")
    producto.cantidad = request.POST.get("cantidad")
    producto.save()


    return HttpResponseRedirect('/ejemplocrud/')


def login(request):
    if request.method == "GET":
        return render(request, 'exo/login.html', {"msg": ""})
    nombre = request.POST.get("nombre", "")
    contrasena = request.POST.get("contrasena", "")
    print("---")
    print("Nombre: "+nombre)
    print("PWD: "+contrasena)
    print("----")
    usuario = Usuario.objects.filter(nombre=nombre)
    if len(usuario) == 0 or usuario[0].contrasenia != contrasena:
        return render(request, 'exo/login.html', {"msg": "Error al iniciar sesión"})
    else:
        return HttpResponseRedirect( '/ejemplocrud/')


