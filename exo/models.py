from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    email = models.Field(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField
    genero = models.CharField(max_length=1)
    contrasenia = models.CharField(max_length=150)

    def crearCliente(self):
        self.save()

    def __str__(self):
        return self.email

class Usuario(models.Model):
    nombre = models.CharField(max_length=10)
    contrasenia = models.CharField(max_length=150)

    def crearUsuario(self):
        self.save()

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    valor = models.IntegerField
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField
    descripcion = models.TextField

    def crearProducto(self):
        self.save()

    def __str__(self):
        return self.nombre