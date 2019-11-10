from django.shortcuts import render
from .models import Usuario

# Create your views here.


def post_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'blog/post_list.html', {'jh': usuarios})