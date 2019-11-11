from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name='index'),
    path('login/', views.login, name='login'),
    path('menucafe/', views.menu_cafe, name='menu_cafe'),
    path('registro/', views.registro, name='registro'),
    path('usuario/<int:pk>/', views.detalle_usuario, name='detalle_usuario'),
]