from django.shortcuts import render, get_object_or_404
from .models import Usuario
from django.http import HttpResponseRedirect

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
    return render(request, 'exo/menucafe.html')

def registro(request):
    return render(request, 'exo/cuestionario.html')

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
        return HttpResponseRedirect('/admin/')


